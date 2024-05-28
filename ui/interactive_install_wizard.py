import os
import customtkinter as ctk
from tkinter import ttk, messagebox
from rich.console import Console
from ansible_utils.inventory import get_host_nicknames
from ansible_utils.roles import Tools
from ansible_utils.ansible_executor import install_tool
from ansible_utils.check_tool import check_tool_remote
from db.database import init_db, log_installation, check_installation

console = Console()

class InteractiveInstallWizard:

    def __init__(self, parent):
        self.parent = parent
        self.steps = [self.config_path_step, self.select_host_step, self.select_tool_step, self.select_version_step]
        self.current_step = 0
        self.config_path = ''
        self.selected_host = ''
        self.selected_tool = ''
        self.version = ''
        self.host_nicknames = []
        self.tool_list = list(Tools)
        self.init_db()
        self.show_step()

    def init_db(self):
        init_db()

    def clear_frame(self):
        for widget in self.parent.winfo_children():
            widget.destroy()

    def show_step(self):
        self.clear_frame()
        step_function = self.steps[self.current_step]
        step_function()

    def next_step(self):
        self.current_step += 1
        self.show_step()

    def previous_step(self):
        self.current_step -= 1
        self.show_step()

    def config_path_step(self):
        from .buttons import show_main_buttons

        default_config_path = os.path.expanduser("~/.ssh/config")
        config_path_label = ctk.CTkLabel(self.parent, text=f"Config Path (default is {default_config_path}):")
        config_path_label.pack(pady=5)
        config_path_entry = ctk.CTkEntry(self.parent)
        config_path_entry.pack(pady=5)

        def on_next():
            self.config_path = config_path_entry.get() or default_config_path
            self.next_step()

        next_button = ctk.CTkButton(self.parent, text="Next", command=on_next)
        next_button.pack(pady=20)

        cancel_button = ctk.CTkButton(self.parent, text="Cancel", command=lambda: show_main_buttons(self.parent))
        cancel_button.pack(pady=10)

    def select_host_step(self):
        from .buttons import show_return_button

        try:
            self.host_nicknames = get_host_nicknames(config_path=self.config_path)
            if not self.host_nicknames:
                messagebox.showerror("Error", "No hosts found in the SSH config file.")
                return

            table_frame = ctk.CTkFrame(self.parent)
            table_frame.pack(fill="both", expand=True)

            table = ttk.Treeview(table_frame, columns=("Number", "Host Nickname"), show='headings')
            table.heading("Number", text="Number")
            table.heading("Host Nickname", text="Host Nickname")

            for index, nickname in enumerate(self.host_nicknames, start=1):
                table.insert("", "end", values=(index, nickname))

            table.pack(fill="both", expand=True)

            def on_next():
                try:
                    selected_item = table.selection()[0]
                    self.selected_host = table.item(selected_item, "values")[1]
                    self.next_step()
                except IndexError:
                    messagebox.showerror("Error", "Please select a host.")

            next_button = ctk.CTkButton(self.parent, text="Next", command=on_next)
            next_button.pack(pady=20)

            back_button = ctk.CTkButton(self.parent, text="Back", command=self.previous_step)
            back_button.pack(pady=10)
        except Exception as e:
            console.print_exception()
            messagebox.showerror("Error", str(e))
            show_return_button(self.parent)

    def select_tool_step(self):
        from .buttons import show_return_button

        try:
            table_frame = ctk.CTkFrame(self.parent)
            table_frame.pack(fill="both", expand=True)

            tool_table = ttk.Treeview(table_frame, columns=("Number", "Tool", "Status"), show='headings')
            tool_table.heading("Number", text="Number")
            tool_table.heading("Tool", text="Tool")
            tool_table.heading("Status", text="Status")

            for index, tool in enumerate(self.tool_list, start=1):
                installed_in_db = check_installation(self.selected_host, tool.name)
                status = "(present)" if installed_in_db else "(absent)"
                tool_table.insert("", "end", values=(index, tool.name, status))

            tool_table.pack(fill="both", expand=True)

            def on_next():
                try:
                    selected_tool_item = tool_table.selection()[0]
                    self.selected_tool = tool_table.item(selected_tool_item, "values")[1]
                    self.next_step()
                except IndexError:
                    messagebox.showerror("Error", "Please select a tool.")

            next_button = ctk.CTkButton(self.parent, text="Next", command=on_next)
            next_button.pack(pady=20)

            back_button = ctk.CTkButton(self.parent, text="Back", command=self.previous_step)
            back_button.pack(pady=10)
        except Exception as e:
            console.print_exception()
            messagebox.showerror("Error", str(e))
            show_return_button(self.parent)

    def select_version_step(self):
        from .buttons import show_main_buttons, show_return_button

        try:
            installed, available_versions = check_tool_remote(self.selected_host, self.selected_tool)
            version_label = ctk.CTkLabel(self.parent, text=f"Installed: {installed}\nAvailable: {available_versions}")
            version_label.pack(pady=5)

            version_combo = ctk.CTkComboBox(self.parent, values=available_versions)
            version_combo.pack(pady=5)

            def on_next():
                self.version = version_combo.get()
                install_tool(self.selected_host, self.selected_tool, self.version, console)
                log_installation(self.selected_host, self.selected_tool, self.version)
                messagebox.showinfo("Success", "Tool installed successfully!")
                show_main_buttons(self.parent)

            next_button = ctk.CTkButton(self.parent, text="Next", command=on_next)
            next_button.pack(pady=20)

            back_button = ctk.CTkButton(self.parent, text="Back", command=self.previous_step)
            back_button.pack(pady=10)
        except Exception as e:
            console.print_exception()
            messagebox.showerror("Error", str(e))
            show_return_button(self.parent)

def show_interactive_install(frame):
    InteractiveInstallWizard(frame)
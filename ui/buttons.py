import customtkinter as ctk
from ui.set_target import show_set_target
from ui.check_state import show_check_state
from ui.utils import clear_frame
from .interactive_install_wizard import show_interactive_install

def show_main_buttons(frame):
    clear_frame(frame)

    # Configure the grid columns to expand proportionally
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)
    frame.grid_columnconfigure(2, weight=1)

    set_target_button = ctk.CTkButton(frame, text="Set Target", command=lambda: show_set_target(frame))
    set_target_button.grid(row=0, column=0, padx=20, pady=20)

    install_button = ctk.CTkButton(frame, text="Interactive Install", command=lambda: show_interactive_install(frame))
    install_button.grid(row=0, column=1, padx=20, pady=20)

    check_state_button = ctk.CTkButton(frame, text="Check State", command=lambda: show_check_state(frame))
    check_state_button.grid(row=0, column=2, padx=20, pady=20)

def show_return_button(frame):
    clear_frame(frame)
    return_button = ctk.CTkButton(frame, text="Return to Homepage", command=lambda: show_main_buttons(frame))
    return_button.pack(pady=20)

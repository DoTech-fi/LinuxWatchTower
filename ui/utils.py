import os

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def display_readme():
    readme_path = os.path.join(os.path.dirname(__file__), '..', 'README.md')
    if os.path.exists(readme_path):
        os.system(f"xdg-open {readme_path}")

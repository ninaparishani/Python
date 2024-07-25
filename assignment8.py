"""Create a python user interface app that is a basic notepad.
 It will be a large textbox inside the window.
 Only basic text will be allowed so no formatting is required.
 At the top of the form, Will be a menu with save, save as, and copy and paste functions.
 Create new files or save over existing ones using the text that is in the textbox."""

import tkinter as tk
from tkinter.filedialog import asksaveasfilename

current_file = None

def save_file():
    global current_file
    if current_file:
        with open(current_file, "w") as file:
            file.write(textbox.get(1.0, tk.END))
    else:
        save_as_file()

def save_as_file():
    global current_file
    file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        current_file = file_path
        with open(current_file, "w") as file:
            file.write(textbox.get(1.0, tk.END))


def copy_text():
    selected_text = textbox.get(tk.SEL_FIRST, tk.SEL_LAST)
    window.clipboard_clear()
    window.clipboard_append(selected_text)


def paste_text():
    clipboard_text = window.clipboard_get()
    textbox.insert(tk.INSERT, clipboard_text)

window = tk.Tk()
window.title("Basic Notepad")

# Textbox
textbox = tk.Text(window, wrap="word")
textbox.pack( fill="both")

# Menu
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)

# Edit Menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)




window.mainloop()
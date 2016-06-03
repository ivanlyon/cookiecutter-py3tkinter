import tkinter
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename

def popupDialog(title, body):
    _dialog = tkinter.Tk()
    _dialog.wm_title(title)
    _dialog.geometry('220x120')

    _label = ttk.Label(_dialog, text=body)
    _label.pack(side="top", fill="x", pady=10)

    _button = ttk.Button(_dialog, text="OK", command = _dialog.destroy)
    _button.pack(side="bottom", pady=10)

    _dialog.mainloop()

def NewFileDialog():
    popupDialog("New button pressed", "Not yet implemented")

def OpenFileDialog():
    _name = tkinter.filedialog.askopenfilename()
    if isinstance(_name, str):
        print ('File selected for open: ' + _name)
    else:
        print ('No file selected')

def AboutDialog():
    _description = "{{cookiecutter.short_description}}"
    if _description == "":
        _description = "No description available"
    _description += '\n'
    _description += '\nAuthor: {{cookiecutter.full_name}}'
    _description += '\nEmail: {{cookiecutter.email}}'
    _description += '\nVersion: {{cookiecutter.version}}'
    _description += '\nGitHub Package: {{cookiecutter.repo_name}}'
    popupDialog("About {{cookiecutter.display_name}}", _description)

def HelpDialog():
    _description = "Not yet created."
    popupDialog("{{cookiecutter.display_name}}", _description)

root = tkinter.Tk()
menu = tkinter.Menu(root)
root.config(menu=menu)
root.wm_title("{{cookiecutter.display_name}}")

filemenu = tkinter.Menu(menu)
filemenu.add_command(label="New", command=NewFileDialog)
filemenu.add_command(label="Open", command=OpenFileDialog)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit)

helpmenu = tkinter.Menu(menu)
helpmenu.add_command(label="Help", command=HelpDialog, accelerator="F1")
helpmenu.add_command(label="About", command=AboutDialog)

menu.add_cascade(label="File", menu=filemenu)
menu.add_cascade(label="Help", menu=helpmenu)

#root.bind('<F1>', lambda event: HelpDialog)

tkinter.mainloop()

"""
{{cookiecutter.repo_name}}
-----------------

{{cookiecutter.short_description}}
"""

import datetime
import sys
import time
import tkinter
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename


class PopupDialog(ttk.Frame):
    "Sample popup dialog implemented to provide feedback."

    def __init__(self, parent, title, body):
        ttk.Frame.__init__(self, parent)
        self.top = tkinter.Toplevel(parent)
        _label = ttk.Label(self.top, text=body, justify=tkinter.LEFT)
        _label.pack(padx=10, pady=10)
        _button = ttk.Button(self.top, text="OK", command=self.ok_button)
        _button.pack(pady=5)
# TODO: set PopupDialog title

    def ok_button(self):
        "OK button feedback."

        self.top.destroy()


class NavigationBar(ttk.Frame):
    "Sample navigation pane provided by cookiecutter switch."

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.config(border=1, relief=tkinter.GROOVE)

        self.scrollbar = ttk.Scrollbar(self, orient=tkinter.VERTICAL)
        self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y, expand=1)

        self.listbox = tkinter.Listbox(self, bg='white')
        self.listbox.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
        for i in range(1, 100):
            self.listbox.insert(tkinter.END, "Navigation " + str(i))
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        self.bind_all('<<ListboxSelect>>', self.onselect)
        self.pack()

    def onselect(self, event):
        """Sample function provided to show how navigation commands may be \
        received."""

        widget = event.widget
        _index = int(widget.curselection()[0])
        _value = widget.get(_index)
        print('List item %d / Navigation %s' % (_index, _value))


class StatusBar(ttk.Frame):
    "Sample status bar provided by cookiecutter switch."
# TODO: add sample status updates such as mouse events
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.labels = []
        self.config(border=1, relief=tkinter.GROOVE)
        for i in range(1, 5):
            _label_text = "Status " + str(i)
            self.labels.append(ttk.Label(self, text=_label_text))
            self.labels[i - 1].config(relief=tkinter.GROOVE)
            self.labels[i - 1].pack(side=tkinter.LEFT, fill=tkinter.X)
        self.pack()


class ToolBar(ttk.Frame):
    "Sample toolbar provided by cookiecutter switch."

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.buttons = []
        self.config(border=1, relief=tkinter.GROOVE)
        for i in range(1, 5):
            _button_text = "Tool " + str(i)
            self.buttons.append(ttk.Button(self, text=_button_text,
                                           command=lambda i=i:
                                           self.run_tool(i)))
            self.buttons[i - 1].pack(side=tkinter.LEFT, fill=tkinter.X)
        self.pack()

    def run_tool(self, number):
        "Sample function provided to show how a toolbar command may be used."

        print('Toolbar button', number, 'pressed')


class MainFrame(ttk.Frame):
    "Main area of user interface content."

    past_time = datetime.datetime.now()
    _advertisement = "Cookiecutter: Open-Source Project Templates"
    _product = "Template: {{cookiecutter.display_name}}"
    _boilerplate = _advertisement + '\n\n' + _product + '\n\n'

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.display = ttk.Label(parent, anchor=tkinter.CENTER,
                                 foreground='green', background='black')
        self.display.pack(fill=tkinter.BOTH, expand=1)
        self.tick()

    def tick(self):
        "Invoked automatically to update a clock displayed in the GUI."

        this_time = datetime.datetime.now()
        if this_time != self.past_time:
            self.past_time = this_time
            _timestamp = this_time.strftime("%Y-%m-%d %H:%M:%S")
            self.display.config(text=self._boilerplate + _timestamp)
        self.display.after(100, self.tick)


class MenuBar(tkinter.Menu):
    "Menu bar appearing with expected components."

    def __init__(self, parent):
        tkinter.Menu.__init__(self, parent)

        filemenu = tkinter.Menu(self, tearoff=False)
        filemenu.add_command(label="New", command=self.new_dialog)
        filemenu.add_command(label="Open", command=self.open_dialog)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1, command=self.quit)

        helpmenu = tkinter.Menu(self, tearoff=False)
        helpmenu.add_command(label="Help", command=self.help_dialog,
                             accelerator="F1")
        helpmenu.add_command(label="About", command=self.about_dialog)
# TODO: show help when F1 is caught
#        self.bind_all('<F1>', lambda event: self.helpDialog)

        self.add_cascade(label="File", underline=0, menu=filemenu)
        self.add_cascade(label="Help", underline=0, menu=helpmenu)

    def quit(self):
        "Ends toplevel execution."

        sys.exit(0)

    def help_dialog(self):
        "Dialog cataloging results achievable, and provided means available."

        _description = "Not yet created."
        PopupDialog(self, "{{cookiecutter.display_name}}", _description)

    def about_dialog(self):
        "Dialog concerning information about entities responsible for program."

        _description = "{{cookiecutter.short_description}}"
        if _description == "":
            _description = "No description available"
        _description += '\n'
        _description += '\nAuthor: {{cookiecutter.full_name}}'
        _description += '\nEmail: {{cookiecutter.email}}'
        _description += '\nVersion: {{cookiecutter.version}}'
        _description += '\nGitHub Package: {{cookiecutter.repo_name}}'
        PopupDialog(self, "About {{cookiecutter.display_name}}", _description)

    def new_dialog(self):
        "Non-functional dialog indicating successful navigation."

        PopupDialog(self, "New button pressed", "Not yet implemented")

    def open_dialog(self):
        "Standard askopenfilename() invocation and result handling."

        _name = tkinter.filedialog.askopenfilename()
        if isinstance(_name, str):
            print('File selected for open: ' + _name)
        else:
            print('No file selected')


class Application(tkinter.Tk):
    "Create top-level Tkinter widget containing all other widgets."

    def __init__(self):
        tkinter.Tk.__init__(self)
        menubar = MenuBar(self)
        self.config(menu=menubar)
        self.wm_title("{{cookiecutter.display_name}}")
        self.wm_geometry("640x480")

# TODO: improve insert_status switch implementation
        if "{{cookiecutter.insert_status}}" == "True":
            self.statusbar = StatusBar(self)
            self.statusbar.pack(side="bottom", fill="x")

# TODO: improve insert_navigation switch implementation
        if "{{cookiecutter.insert_navigation}}" == "True":
            self.navigationbar = NavigationBar(self)
            self.navigationbar.pack(side="left", fill="y")

# TODO: improve insert_toolbar switch implementation
        if "{{cookiecutter.insert_toolbar}}" == "True":
            self.toolbar = ToolBar(self)
            self.toolbar.pack(side="top", fill="x")

        self.mainframe = MainFrame(self)
        self.mainframe.pack(side="right", fill="y")

if __name__ == "__main__":
    APPLICATION_GUI = Application()
    APPLICATION_GUI.mainloop()

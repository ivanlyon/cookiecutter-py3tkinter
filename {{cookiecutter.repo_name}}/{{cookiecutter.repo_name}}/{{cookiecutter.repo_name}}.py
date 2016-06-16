"""
{{cookiecutter.repo_name}}
-----------------

{{cookiecutter.short_description}}
"""

import datetime
import gettext
import sys
import time
import tkinter
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename

# All translations provided for illustrative purposes only.
{% if cookiecutter.language == 'german' %}
de = gettext.translation('messages', localedir='locale', languages=['de'])
de.install()
{% elif cookiecutter.language == 'spanish' %}
es = gettext.translation('messages', localedir='locale', languages=['es'])
es.install()
{% else %} # english
_ = lambda s: s
{% endif %}


class PopupDialog(ttk.Frame):
    "Sample popup dialog implemented to provide feedback."

    def __init__(self, parent, title, body):
        ttk.Frame.__init__(self, parent)
        self.top = tkinter.Toplevel(parent)
        _label = ttk.Label(self.top, text=body, justify=tkinter.LEFT)
        _label.pack(padx=10, pady=10)
        _button = ttk.Button(self.top, text=_("OK"), command=self.ok_button)
        _button.pack(pady=5)
        self.top.title(title)

    def ok_button(self):
        "OK button feedback."

        self.top.destroy()


{% if cookiecutter.insert_navigation == 'y' %}
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
            self.listbox.insert(tkinter.END, _('Navigation ') + str(i))
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
        print(_('List item'), ' %d / %s' % (_index, _value))
{% endif %}


{% if cookiecutter.insert_status == 'y' %}
class StatusBar(ttk.Frame):
    "Sample status bar provided by cookiecutter switch."
    _status_bars = 4

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.labels = []
        self.config(border=1, relief=tkinter.GROOVE)
        for i in range(self._status_bars):
            _label_text = _('Unset status ') + str(i + 1)
            self.labels.append(ttk.Label(self, text=_label_text))
            self.labels[i].config(relief=tkinter.GROOVE)
            self.labels[i].pack(side=tkinter.LEFT, fill=tkinter.X)
        self.pack()

    def set_text(self, status_index, new_text):
        self.labels[status_index].config(text=new_text)
{% endif %}


{% if cookiecutter.insert_toolbar == 'y' %}
class ToolBar(ttk.Frame):
    "Sample toolbar provided by cookiecutter switch."

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.buttons = []
        self.config(border=1, relief=tkinter.GROOVE)
        for i in range(1, 5):
            _button_text = _('Tool ') + str(i)
            self.buttons.append(ttk.Button(self, text=_button_text,
                                           command=lambda i=i:
                                           self.run_tool(i)))
            self.buttons[i - 1].pack(side=tkinter.LEFT, fill=tkinter.X)
        self.pack()

    def run_tool(self, number):
        "Sample function provided to show how a toolbar command may be used."

        print(_('Toolbar button'), number, _('pressed'))
{% endif %}


class MainFrame(ttk.Frame):
    "Main area of user interface content."

    past_time = datetime.datetime.now()
    _advertisement = 'Cookiecutter: Open-Source Project Templates'
    _product = _('Template') + ': {{cookiecutter.display_name}}'
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
            _timestamp = this_time.strftime('%Y-%m-%d %H:%M:%S')
            self.display.config(text=self._boilerplate + _timestamp)
        self.display.after(100, self.tick)


class MenuBar(tkinter.Menu):
    "Menu bar appearing with expected components."

    def __init__(self, parent):
        tkinter.Menu.__init__(self, parent)

        filemenu = tkinter.Menu(self, tearoff=False)
        filemenu.add_command(label=_('New'), command=self.new_dialog)
        filemenu.add_command(label=_('Open'), command=self.open_dialog)
        filemenu.add_separator()
        filemenu.add_command(label=_('Exit'), underline=1,
                             command=self.quit)

        helpmenu = tkinter.Menu(self, tearoff=False)
        helpmenu.add_command(label=_('Help'), command=lambda:
                             self.help_dialog(None), accelerator="F1")
        helpmenu.add_command(label=_('About'), command=self.about_dialog)
        self.bind_all('<F1>', self.help_dialog)

        self.add_cascade(label=_('File'), underline=0, menu=filemenu)
        self.add_cascade(label=_('Help'), underline=0, menu=helpmenu)

    def quit(self):
        "Ends toplevel execution."

        sys.exit(0)

    def help_dialog(self, event):
        "Dialog cataloging results achievable, and provided means available."

        _description = _('Help not yet created.')
        PopupDialog(self, '{{cookiecutter.display_name}}', _description)

    def about_dialog(self):
        "Dialog concerning information about entities responsible for program."

        _description = '{{cookiecutter.short_description}}'
        if _description == '':
            _description = _('No description available')
        _description += '\n'
        _description += '\n' + _('Author') + ': {{cookiecutter.full_name}}'
        _description += '\n' + _('Email') + ': {{cookiecutter.email}}'
        _description += '\n' + _('Version') + ': {{cookiecutter.version}}'
        _description += '\n' + _('GitHub Package') + \
                        ': {{cookiecutter.repo_name}}'
        PopupDialog(self, _('About') + ' {{cookiecutter.display_name}}',
                    _description)

    def new_dialog(self):
        "Non-functional dialog indicating successful navigation."

        PopupDialog(self, _('New button pressed'), _('Not yet implemented'))

    def open_dialog(self):
        "Standard askopenfilename() invocation and result handling."

        _name = tkinter.filedialog.askopenfilename()
        if isinstance(_name, str):
            print(_('File selected for open: ') + _name)
        else:
            print(_('No file selected'))


class Application(tkinter.Tk):
    "Create top-level Tkinter widget containing all other widgets."

    def __init__(self):
        tkinter.Tk.__init__(self)
        menubar = MenuBar(self)
        self.config(menu=menubar)
        self.wm_title('{{cookiecutter.display_name}}')
        self.wm_geometry('640x480')

{% if cookiecutter.insert_status == 'y' %}# Status bar selection == 'y'
        self.statusbar = StatusBar(self)
        self.statusbar.pack(side='bottom', fill='x')
        self.bind_all('<Enter>', lambda e: self.statusbar.set_text(0,
                      'Mouse: 1'))
        self.bind_all('<Leave>', lambda e: self.statusbar.set_text(0,
                      'Mouse: 0'))
        self.bind_all('<Button-1>', lambda e: self.statusbar.set_text(1,
                      'Clicked at x = ' + str(e.x) + ' y = ' + str(e.y)))
        self.start_time = datetime.datetime.now()
        self.uptime()
{% endif %}

{% if cookiecutter.insert_navigation == 'y' %}# Navigation selection == 'y'
        self.navigationbar = NavigationBar(self)
        self.navigationbar.pack(side='left', fill='y')
{% endif %}

{% if cookiecutter.insert_toolbar == 'y' %}# Tool bar selection == 'y'
        self.toolbar = ToolBar(self)
        self.toolbar.pack(side='top', fill='x')
{% endif %}

        self.mainframe = MainFrame(self)
        self.mainframe.pack(side='right', fill='y')

{% if cookiecutter.insert_status == 'y' %}# Status bar selection == 'y'
    def uptime(self):
        _upseconds = str(int(round((datetime.datetime.now() - self.start_time).total_seconds())))
        self.statusbar.set_text(2, _('Uptime') + ': ' + _upseconds)
        self.after(1000, self.uptime)
{% endif %}

if __name__ == '__main__':
    APPLICATION_GUI = Application()
    APPLICATION_GUI.mainloop()

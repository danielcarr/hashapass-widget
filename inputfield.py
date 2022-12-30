import tkinter as tk
import tkinter.ttk as ttk


class InputField(ttk.Entry):

    def __init__(self, master=None, placeholder=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.placeholder = placeholder

        self.bind('<FocusIn>', self.gained_focus)
        self.bind('<FocusOut>', self.lost_focus)

        self.isupdating = None
        self.set_empty(True)

        if 'textvariable' in kwargs:
            kwargs['textvariable'].trace_add('write', self.text_changed)

    def set_empty(self, isempty):
        self.isempty = isempty
        self.isupdating = True
        if isempty:
            self.originalforeground = self['foreground']
            self.originalshow = self['show']
            self.configure(foreground='darkgrey', show='')
            self.delete(0, tk.END)
            if not self.instate(['focus']):
                self.insert(0, self.placeholder)
        else:
            self.configure(foreground=self.originalforeground)
            self.configure(show=self.originalshow)
            self.delete(0, tk.END)
        self.isupdating = False

    def gained_focus(self, *args):
        if self.isempty:
            self.set_empty(False)

    def lost_focus(self, *args):
        text = self.get()
        if text == '':
            self.set_empty(True)

    def configure(self, **kwargs):
        if 'textvariable' in kwargs:
            kwargs['textvariable'].trace_add('write', self.text_changed)

        if not self.instate(['focus']) and not self.isupdating:
            if 'show' in kwargs:
                self.originalshow = kwargs.pop('show')
            if 'foreground' in kwargs:
                self.originalforeground = kwargs.pop('foreground')

        super().configure(**kwargs)

    def get(self):
        if self.isempty:
            return ''
        else:
            return super().get()

    def text_changed(self, *args):
        if self.instate(['focus']) or self.isupdating:
            return
        isempty = self.get() == ''
        self.set_empty(isempty)

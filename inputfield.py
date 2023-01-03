import tkinter as tk
import tkinter.ttk as ttk


class InputField(ttk.Entry):

    def __init__(self, master=None, placeholder='', **kwargs):
        super().__init__(master, **kwargs)

        name = f'{self}-placeholdervariable'
        self.placeholdervariable = tk.StringVar(name=name, value=placeholder)

        self.bind('<FocusIn>', self.gained_focus)
        self.bind('<FocusOut>', self.lost_focus)

        self.isupdating = None
        self.isempty = None
        self.set_empty(True)

        if 'textvariable' in kwargs:
            kwargs['textvariable'].trace_add('write', self.text_changed)

    def set_empty(self, isempty):
        if isempty == self.isempty:
            return

        self.isempty = isempty
        self.isupdating = True
        if isempty:
            self.originalforeground = self['foreground']
            self.originalshow = self['show']
            self.configure(foreground='darkgrey', show='')
            self.delete(0, tk.END)
            self.originalvariable = self['textvariable']
            if not self.instate(['focus']):
                self.configure(textvariable=self.placeholdervariable)
        else:
            self.configure(
                    foreground=self.originalforeground,
                    textvariable=self.originalvariable,
                    show=self.originalshow
                    )
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
        if 'placeholder' in kwargs:
            self.placeholdervariable.set(kwargs.pop('placeholder'))

        if 'textvariable' in kwargs and not self.isupdating:
            kwargs['textvariable'].trace_add('write', self.text_changed)
            if self.isempty and not self.instate(['focus']):
                self.originalvariable = kwargs.pop('textvariable')

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

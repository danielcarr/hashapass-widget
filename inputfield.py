import tkinter.ttk as ttk


class InputField(ttk.Entry):

    def __init__(self, parent=None, placeholder=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.placeholder = placeholder

        self.bind('<FocusIn>', self.gained_focus)
        self.bind('<FocusOut>', self.lost_focus)

        self.set_empty(True)

    def set_empty(self, isempty):
        self.isempty = isempty
        if isempty:
            self.originalforeground = self['foreground']
            self.originalshow = self['show']
            self.configure(foreground='darkgrey', show='')
            if self.instate(['focus']):
                self.delete(0, 'end')
            else:
                self.insert(0, self.placeholder)
        else:
            self.delete(0, 'end')
            self.configure(foreground=self.originalforeground)
            self.configure(show=self.originalshow)

    def gained_focus(self, *args):
        if self.isempty:
            self.set_empty(False)

    def lost_focus(self, *args):
        text = self.get()
        if text == '' or text is None:
            self.set_empty(True)
        else:
            self.set_empty(False)
            self.insert(0, text)

    def get(self):
        if self.isempty:
            return ''
        else:
            return super().get()

    def set(self, value):
        if value == '' or value is None:
            self.set_empty(True)
        elif self.isempty:
            self.set_empty(False)
            super().set(value)

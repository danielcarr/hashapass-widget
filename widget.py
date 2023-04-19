#! /usr/bin/env python3

import tkinter as tk
import tkinter.ttk as ttk

import hashapass
from inputfield import InputField


class HashapassWidget:

    def __init__(self, window):

        # Setup container
        self.window = window
        self.window.resizable(width=False, height=False)
        self.window.title('Password Generator')
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

        frame = ttk.Frame(window, padding='1 1 1 1')
        frame.grid(column=0, row=0, sticky=(tk.N, tk.E, tk.W, tk.S))

        # Field variables
        self.character_count = tk.IntVar(value=10)
        self.parameter = tk.StringVar()
        self.password = tk.StringVar()
        self.result = tk.StringVar()

        # Input fields
        self.entry_parameter = InputField(
                frame, placeholder='Parameter',
                width=20, textvariable=self.parameter)

        self.entry_master_password = InputField(
                frame, placeholder='Master Password',
                width=16, show='*', textvariable=self.password)

        spinbox_length = ttk.Spinbox(
                frame, width=2, from_=8, to=32, increment=1,
                state='readonly', textvariable=self.character_count)

        # Output display field
        entry_generated_password = ttk.Entry(
                frame, width=16, font='TkFixedFont',
                state='readonly', takefocus=0, textvariable=self.result)

        # Bind events
        self.window.bind('<Return>', self.generate_password)
        self.window.bind('<Escape>', self.reset)
        entry_generated_password.bind('<Double-Button-1>', self.copy_password)

        # Layout widgets
        horizontal = (tk.W, tk.E)
        self.entry_parameter.grid(column=0, row=0, sticky=horizontal)
        self.entry_master_password.grid(column=1, row=0, sticky=horizontal)
        spinbox_length.grid(column=2, row=0, sticky=horizontal)
        entry_generated_password.grid(column=3, row=0, sticky=horizontal)

        for child in self.window.winfo_children():
            child.grid_configure(padx=5, pady=2)

        # Set initial UI state
        self.reset()

    def copy_password(self, event):
        self.window.clipboard_clear()
        self.window.clipboard_append(self.result.get())
        if event.type.startswith('Button'):
            event.widget.selection_range(0, tk.END)
            # Stop processing bindings to prevent partial text selection
            return 'break'

    def reset(self, *args):
        self.parameter.set('')
        self.password.set('')
        self.result.set('')
        self.entry_parameter.focus()

    def generate_password(self, event):
        password = self.password.get()
        parameter = self.parameter.get()

        if parameter == '':
            self.entry_parameter.focus()
            return
        if password == '':
            self.entry_master_password.focus()
            return

        length = self.character_count.get()

        self.result.set(hashapass.generate(parameter, password, length))

        self.copy_password(event)

        self.entry_parameter.focus()
        self.entry_parameter.selection_range(0, tk.END)


if __name__ == '__main__':
    window = tk.Tk()
    HashapassWidget(window)
    window.mainloop()

#! /usr/bin/env python3

import base64
import hmac
import tkinter as tk
import tkinter.ttk as ttk

from inputfield import InputField


class HashapassWidget:

    def __init__(self, window):

        self.window = window
        self.window.resizable(width=False, height=False)
        self.window.title('Password Generator')
        self.window.bind('<Return>', self.generate_password)
        self.window.bind('<Escape>', self.reset)

        frame = ttk.Frame(window, padding="1 1 1 1")
        frame.grid(column=0, row=0, sticky=(tk.N, tk.E, tk.W, tk.S))
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

        self.parameter = tk.StringVar()
        self.entry_parameter = InputField(frame, placeholder='Parameter', width=20, textvariable=self.parameter)
        self.entry_parameter.grid(column=0, row=0, sticky=(tk.W, tk.E))

        self.password = tk.StringVar()
        entry_master_password = InputField(frame, placeholder='Password', width=16, textvariable=self.password, show='*')
        entry_master_password.grid(column=1, row=0, sticky=(tk.W, tk.E))

        self.character_count = tk.IntVar(value=10)
        spinbox_length = ttk.Spinbox(frame, width=2, from_=8, to=32, increment=1, state='readonly', textvariable=self.character_count)
        spinbox_length.grid(column=2, row=0, sticky=(tk.W, tk.E))

        self.result = tk.StringVar()
        self.entry_generated_password = ttk.Entry(frame, width=16, state='readonly', textvariable=self.result)
        self.entry_generated_password.grid(column=3, row=0, sticky=(tk.W, tk.E))

        for child in self.window.winfo_children():
            child.grid_configure(padx=5, pady=2)

        self.reset()

    def reset(self, *args):
        self.parameter.set('')
        self.password.set('')
        self.result.set('')
        self.entry_parameter.focus()

    def generate_password(self, *args):
        key = bytes(self.password.get(), 'utf-8')
        parameter = self.parameter.get().encode('utf-8')
        digest = hmac.new(key, msg=parameter, digestmod='sha1').digest()
        self.result.set(str(base64.b64encode(digest)[:self.character_count.get()], 'utf-8'))
        self.window.clipboard_clear()
        self.window.clipboard_append(self.result.get())


if __name__ == '__main__':
    window = tk.Tk()
    HashapassWidget(window)
    window.mainloop()

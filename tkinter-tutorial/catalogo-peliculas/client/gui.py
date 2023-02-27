import tkinter as tk

class Frame(tk.Frame):
    def __init__(self, root=None):
        self.root = root
        self.pack(fill='both', expand=1)
            # fill option added to make widget fill entire frame.
            # expand option added to expand widget, if user resizes frame.
        self.config(bg='lightblue')
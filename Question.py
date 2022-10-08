import tkinter as tk
from data import answer_vars

class Question:
    def __init__(self, parent, q, a):

        self.frame = tk.Frame(parent.frame)

        self.lbl = tk.Label(self.frame, text = q, font = (18))
        self.lbl.grid(row = 0)

        self.var = tk.StringVar(value = "none")

        self.btns = []
        for i, text in a.items():
            btn = tk.Radiobutton(self.frame, text = text, value = i, variable = self.var)
            btn.grid()
            self.btns.append(btn)

    def start(self):
        self.frame.grid(row=0)

    def end(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
            self.frame.place_forget()




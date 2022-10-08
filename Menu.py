import tkinter as tk
from tkinter import font
from Question import *
from Quiz import Quiz

class Menu:
    def __init__(self, parent):

        self.frame = tk.Frame(parent)

        self.lbl = tk.Label(self.frame, text = "Добро пожаловать на тестирование!", font = (18))
        self.lbl.grid(row = 0)

        self.btn = tk.Button(self.frame, text = "Начать", font = 12, command = self.btnstart)
        self.btn.grid(row = 1, pady = 24)
        

        self.btn2 = tk.Button(self.frame, text = "О разработчиках ", font = 12, command = self.btnrazrab)
        self.btn2.grid(row = 2, pady = 24)
        self.frame.pack()

    def btnrazrab(self):
        self.end()

        self.lbl = tk.Label(self.frame, text= "Сделал: Торопов Александр Александрович. Студент группы ПИ-23", font = 20)
        self.lbl.grid(row = 0, pady= 40)
        self.frame.pack()

        self.startbtn = tk.Button(self.frame, text = "Начать тестирование", font = 24, command = self.btnstart)
        self.startbtn.grid(row= 2, pady = 24)

    def btnstart(self):
        self.end()
        quiz = Quiz(self)
        quiz.start()
     
        
    
    def start(self):
        self.frame.place(relx =.5, rely =.5,anchor = "center")


    def end(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
            self.frame.place_forget()


    
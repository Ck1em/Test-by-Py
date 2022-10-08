import tkinter as tk
from Menu import Menu
from Question import Question

window = tk.Tk()

window.geometry("700x400")
window.title("Программа для тестирования ")

menu = Menu(window)
menu.start()



window.mainloop()
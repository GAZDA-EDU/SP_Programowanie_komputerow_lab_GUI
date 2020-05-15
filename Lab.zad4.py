from random import randint
import tkinter as tk


def zlapMnie(e=None):
    b.place(x = randint(0,435),y= randint(0,475))
    

okno = tk.Tk()
okno.title("Złap mnie!")
b = tk.Button(okno, text="Złap mnie")
b.place(x=10,y=10)
okno = tk.Frame(okno.geometry("500x500"))

b.bind("<Enter>", zlapMnie)

okno.mainloop()
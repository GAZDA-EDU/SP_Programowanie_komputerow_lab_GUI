from tkinter import *


def zmiana_1():
    global c
    c.itemconfig(s1, fill='red')
    c.itemconfig(s2, fill='yellow')
    c.itemconfig(s3, fill='gray')
    c.after(1000,zmiana_2)    
        
def zmiana_2():
    global c
    c.itemconfig(s1, fill='grey')
    c.itemconfig(s2, fill='grey')
    c.itemconfig(s3, fill='green')
    c.after(1000,zmiana_3)

def zmiana_3():
    global c
    c.itemconfig(s1, fill='grey')
    c.itemconfig(s2, fill='yellow')
    c.itemconfig(s3, fill='grey')
    c.after(1000,zmiana_4)
    
def zmiana_4():
    global c
    c.itemconfig(s1, fill='red')
    c.itemconfig(s2, fill='grey')
    c.itemconfig(s3, fill='grey')
    c.after(1000,zmiana_1)


okno = Tk()
okno.title("Sygnalizator")

c = Canvas(okno, width=235, height=450)
c.pack()

s1 = c.create_oval(80,40,160,120, fill='red')
s2 = c.create_oval(80,180,160,260, fill='gray')
s3 = c.create_oval(80,320,160,400, fill='gray')

c.after(1000,zmiana_1)


okno.mainloop()
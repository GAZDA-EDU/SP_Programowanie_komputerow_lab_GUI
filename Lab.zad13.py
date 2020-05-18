from tkinter import *

znaki = []
litery = []
cyfry = []

def czytaj(z=None):
    znak=str(z.char)
    znaki.append(znak) 
    iz = f'Znaków:{len(znaki)}'
    e1.config(state=NORMAL)
    e1.delete(0,END)
    e1.insert(0,iz)
    e1.config(state="readonly")
    if znak.isalpha() == True:
        litery.append(znak)
        il = f'Liter:{len(litery)}'
        e2.config(state=NORMAL)
        e2.delete(0,END)
        e2.insert(0,il)
        e2.config(state="readonly")
    elif znak.isdigit() == True:
        cyfry.append(znak)
        ic = f'Liter:{len(cyfry)}'
        e3.config(state=NORMAL)
        e3.delete(0,END)
        e3.insert(0,ic)
        e3.config(state="readonly")

okno = Tk()
okno.title('Text')

tx=StringVar()
textbox = Text(okno, width=60, height=15)
textbox.grid(row=1,column=1,columnspan=3)
textbox.bind("<Key>", czytaj)


e1 = Entry(okno, state="readonly", readonlybackground="white")
e1.grid(row=2,column=1)

e2 = Entry(okno, state="readonly", readonlybackground="white")
e2.grid(row=2,column=2)

e3 = Entry(okno, state="readonly", readonlybackground="white")
e3.grid(row=2,column=3)


okno.mainloop()
from tkinter import *
from tkinter import messagebox

ox=245
oy=230

def w_gore(e=None):
    global ox,oy
    if oy >= 1:
        oy=oy-1
        b.place(x=ox,y=oy)
    else:
        oy=oy+1
        b.place(x=ox,y=oy)

def w_dol(e=None):
    global ox,oy
    if oy <= 471:
        oy=oy+1
        b.place(x=ox,y=oy)
    else:
        oy=oy-1
        b.place(x=ox,y=oy)

def w_prawo(e=None):
    global ox,oy
    if ox <= 472:
        ox=ox+1
        b.place(x=ox,y=oy)
    else:
        ox=ox-1
        b.place(x=ox,y=oy)

def w_lewo(e=None):
    global ox,oy
    if ox >= 1:
        ox=ox-1
        b.place(x=ox,y=oy)
    else:
        ox=ox+1
        b.place(x=ox,y=oy)

def w_gore_5(e=None):
    global ox,oy
    if oy >= 1:
        oy=oy-5
        b.place(x=ox,y=oy)
    else:
        oy=oy+5
        b.place(x=ox,y=oy)

def w_dol_5(e=None):
    global ox,oy
    if oy <= 471:
        oy=oy+5
        b.place(x=ox,y=oy)
    else:
        oy=oy-5
        b.place(x=ox,y=oy)

def w_prawo_5(e=None):
    global ox,oy
    if ox <= 472:
        ox=ox+5
        b.place(x=ox,y=oy)
    else:
        ox=ox-5
        b.place(x=ox,y=oy)

def w_lewo_5(e=None):
    global ox,oy
    if ox >= 1:
        ox=ox-5
        b.place(x=ox,y=oy)
    else:
        ox=ox+5
        b.place(x=ox,y=oy)

def koniec(e=None):
    global okno
    odp = messagebox.askquestion("Zakończ program", "Czy na pewno chcesz zakończyć?")
    if odp == 'yes':
        okno.destroy()

okno = Tk()
okno.title("Manipulator")

b=Button(okno,bitmap="questhead")
b.place(x=245,y=230)

okno.bind("<Up>", w_gore)
okno.bind("<Down>", w_dol)
okno.bind("<Right>", w_prawo)
okno.bind("<Left>", w_lewo)

okno.bind("<Control-Up>", w_gore_5)
okno.bind("<Control-Down>", w_dol_5)
okno.bind("<Control-Right>", w_prawo_5)
okno.bind("<Control-Left>", w_lewo_5)

okno.bind("<Escape>", koniec)

okno.geometry("500x500")

okno.mainloop()
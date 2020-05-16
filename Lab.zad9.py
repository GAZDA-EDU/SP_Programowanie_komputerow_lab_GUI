from tkinter import *


def iloczyn():
    mnozna = rx.get()
    mnoznik = ry.get()
    wynik = mnozna * mnoznik
    return str(wynik)

def set():
    a=rx.get()
    b=ry.get()
    c=ry.get()
    d=rx.get()
    e=ry.get()
    f=rx.get()
    l["fg"] = '#{}{}{}{}{}{}'.format(a,b,c,d,e,f,)
    tx.set(iloczyn())


okno = Tk()

rx_buttons = []
ry_buttons = []
rx = IntVar()
ry = IntVar()

for i in range(11):
    
    rb_ox = Radiobutton(okno, text=str(i), variable=rx, value=i, command=set)
    rb_ox.grid(row=0,column=i+1)
    rx_buttons.append(rb_ox)

    rb_oy = Radiobutton(okno, text=str(i), variable=ry, value=i, command=set)
    rb_oy.grid(row=i+1,column=0)
    ry_buttons.append(rb_oy)

tx = StringVar()
l = Label(okno, textvariable=tx, font=("Arial", "100", "bold",))
l.place(x=150,y=80)
tx.set(iloczyn())

rx_buttons[0].select()
ry_buttons[0].select()

okno.mainloop()
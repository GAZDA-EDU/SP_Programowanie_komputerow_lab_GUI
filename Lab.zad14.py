from tkinter import *

lista_h = ['0','0','0','0']

def przelicz(p):
    h = str(sbox[p].get())
    h = h.lstrip('0x')
    lista_h[p] = h
    lh = '0x' + ''.join(lista_h)
    ld = int(lh,16)
    e.config(state=NORMAL)
    e.delete(0,END)
    e.insert(END,ld)
    e.config(state="readonly")

okno = Tk()
okno.title('Spinbox')

sbox = []

for i in range(0,4):
    sb = Spinbox(okno, width=6, value=('0x0','0x1','0x2','0x3','0x4','0x5','0x6','0x7','0x8','0x9','0xa','0xb','0xc','0xd','0xe','0xf'), command=(lambda p=i:przelicz(p)))
    sb.grid(row=0,column=i)
    sbox.append(sb)

e = Entry(okno, width=25, justify=RIGHT, readonlybackground="white")
e.grid(row=1,columnspan=4)
e.insert(END, str(0))
e.config(state="readonly")

okno.mainloop()
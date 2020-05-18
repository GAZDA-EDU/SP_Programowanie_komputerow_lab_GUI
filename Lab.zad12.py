from tkinter import *


znak= ''

def cyfry(c):
    e.config(state=NORMAL)
    l = e.get()
    if l == '0':
        e.delete(0,END)
        e.insert(END,c)
    elif l == '.':
        e.delete(0,END)
        e.insert(END,'0.')
        e.insert(END,c)
    elif l.count('.') == 2:
        l = l.rstrip('.')
        e.delete(0,END)
        e.insert(END,l)
        e.insert(END,c)
    elif l == 'ZeroDivisionError':
        e.delete(0,END)
        e.insert(END,c)
    else: 
        e.insert(END,c)
    e.config(state="readonly")

def czysc():
    e.config(state=NORMAL)
    e.delete(0,END)
    e.insert(END,'0')
    e.config(state="readonly")

def plus_minus():
    l = str(e.get())
    if l != '' and l != '.':
        if l.count('.') == 2:
            l = l.rstrip('.')
        e.config(state=NORMAL)
        e.delete(0,END)
        if float(l) > 0:
            e.insert(END, -float(l))
        else:
            e.insert(END, abs(float(l)))
        e.config(state="readonly")
    else:
        e.config(state=NORMAL)
        e.delete(0,END)
        e.insert(END,'')
        e.config(state="readonly")

def dzialanie(z):
    l = e.get()
    global znak, pl
    if l != '' and l != '.':
        pl = float(l)
        znak = z
        e.config(state=NORMAL)
        e.delete(0,END)
        e.insert(END,'')
        e.config(state="readonly")
    else:
        e.config(state=NORMAL)
        e.delete(0,END)
        e.insert(END,'')
        e.config(state="readonly")

def wynik():
    l = e.get()
    if l != '' and l != '.':
        dl = float(l)
        e.config(state=NORMAL)
        e.delete(0,END)
        if znak == '+':
            e.insert(END, pl + dl)
        elif znak == '-':
            e.insert(END, pl - dl)
        elif znak == '*':
            e.insert(END, pl * dl)
        elif znak == '/':
            if dl != '0':
                e.insert(END, pl / dl)
            else:
                e.insert(END, 'ZeroDivisionError')
        else:
            e.delete(0,END)
            e.insert(END,'0')
        e.config(state="readonly")
    else:
        e.config(state=NORMAL)
        e.delete(0,END)
        e.insert(END,'')
        e.config(state="readonly")

okno = Tk()
okno.title("K.")


e = Entry(okno, width=26, justify=RIGHT, readonlybackground="white")
e.grid(row=0,columnspan=5)
e.insert(END, str(0))
e.config(state="readonly")

przyciski_c = []

for i in range(9):
    
    if i < 3:
        przycisk_c = Button(okno, width=3, text=str(i+1), command=(lambda c=i+1:cyfry(str(c))))
        przycisk_c.grid(row=3,column=i)
        przyciski_c.append(przycisk_c)

    elif i >= 3 and i < 6:
        przycisk_c = Button(okno, width=3, text=str(i+1), command=(lambda c=i+1:cyfry(str(c))))
        przycisk_c.grid(row=2,column=i-3)
        przyciski_c.append(przycisk_c)

    else:
        przycisk_c = Button(okno, width=3, text=str(i+1), command=(lambda c=i+1:cyfry(str(c))))
        przycisk_c.grid(row=1,column=i-6)
        przyciski_c.append(przycisk_c)
    
przycisk_0 = Button(okno,width=3, text='0', command=(lambda c=0:cyfry(str(c))))
przycisk_0.grid(row=4,column=0)

przycisk_c = Button(okno,width=3, text='C', command=czysc)
przycisk_c.grid(row=4,column=1)

przycisk_kropka = Button(okno,width=3, text='.', command=(lambda z='.':cyfry(z)))
przycisk_kropka.grid(row=4,column=2)

przycisk_r = Button(okno,width=4, text='=', command=wynik)
przycisk_r.grid(row=3,column=3)

przycisk_zz = Button(okno,width=4, text='+/-', command=plus_minus)
przycisk_zz.grid(row=4,column=3)

przycisk_dod = Button(okno,width=3,text='+', command=(lambda z='+':dzialanie(z)))
przycisk_dod.grid(row=1,column=4)

przycisk_ode = Button(okno,width=3, text='-', command=(lambda z='-':dzialanie(z)))
przycisk_ode.grid(row=2,column=4)

przycisk_mno = Button(okno,width=3, text='*', command=(lambda z='*':dzialanie(z)))
przycisk_mno.grid(row=3,column=4)

przycisk_dzi = Button(okno,width=3, text='/', command=(lambda z='/':dzialanie(z)))
przycisk_dzi.grid(row=4,column=4)



okno.mainloop()
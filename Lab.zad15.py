from tkinter import *
from datetime import date

lm = ('styczeń', 
      'luty', 
      'marzec', 
      'kwiecień', 
      'maj', 
      'czerwiec', 
      'lipiec', 
      'sierpień', 
      'wrzesień', 
      'październik', 
      'listopad', 
      'grudzień')

def info():
    lb2.delete(0,END)
    lb2.insert(END, 'Wybierz miesiąc')
    lb2.config(state="disabled")
    e.config(state=NORMAL)
    e.delete(0,END)
    e.config(state="readonly")

def lb1Select(index1):
    global m, rp, k
    k = lb1.curselection()
    rp = v3.get()
    if k != ():
        e.config(state=NORMAL)
        e.delete(0,END)
        e.config(state="readonly")
        m = k[0] + 1 
        lb2.config(state="normal")
        for m_31 in [1,3,5,7,8,10,12]:
            if m == m_31:
                lb2.delete(0,END)
                for g in range(1,32):
                    lb2.insert(END, g)
        for m_30 in [4,6,9,11]:
            if m == m_30:
                lb2.delete(0,END)
                for h in range(1,31):
                    lb2.insert(END, h)
        if rp == 0 and m == 2:
                lb2.delete(0,END)
                for k in range(1,29):
                    lb2.insert(END, k)
        elif rp == 1 and m == 2:
                lb2.delete(0,END)
                for l in range(1,30):
                    lb2.insert(END, l)

def lb2Select(index2):
    k = lb2.curselection()
    if k != ():
        d = k[0] + 1
        e.config(state=NORMAL)
        if rp == 0:
            delta =  date(2019,12,31) - date(2019,m,d)
            ilosc_dni = delta.days
            dzien = str(365 - ilosc_dni)
            e.delete(0,END)
            e.insert(END,dzien)
        elif rp == 1:
            delta =  date(2020,12,31) - date(2020,m,d)
            ilosc_dni = delta.days
            dzien = str(366 - ilosc_dni)
            e.delete(0,END)
            e.insert(END,dzien)
        e.config(state="readonly")


okno = Tk()
okno.title('Listbox')

v1 = StringVar()
lb1 = Listbox(okno, height=12, listvariable=v1)
lb1.grid(row=0,column=0)
for i in lm:
    lb1.insert(END, i)
lb1.bind('<<ListboxSelect>>', lb1Select) 

v2 = StringVar()
lb2 = Listbox(okno, height=31, listvariable=v2)
lb2.grid(row=0,column=1)
lb2.insert(END, 'Wybierz miesiąc')
lb2.config(state="disabled")
lb2.bind('<<ListboxSelect>>', lb2Select) 

v3 = IntVar()
cb = Checkbutton(okno, text='rok przestępny', variable=v3,command=info)
cb.grid(row=1,columnspan=2)

e = Entry(okno, width=25, justify=RIGHT, state="readonly", readonlybackground="white")
e.grid(row=2,columnspan=2)

okno.mainloop()
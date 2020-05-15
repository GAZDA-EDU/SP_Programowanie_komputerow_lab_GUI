from tkinter import *
from tkinter import messagebox
from random import randint

unikalne_liczby = []
ilosc_przyciskow = 25
while len(unikalne_liczby) < ilosc_przyciskow:
    liczba = randint(1,999)
    if liczba in unikalne_liczby:
        continue
    unikalne_liczby.append(liczba)    

pul = sorted(unikalne_liczby)

def klik(x,p):
    global przyciski, przycisk, pul
    if int(p) == pul[0]:
        przyciski[x].config(state = DISABLED)
        pul.remove(pul[0])
        if pul == []:
            messagebox.showinfo('Gratulacje', 'Pomyślnie ukończyłeś zadanie')
            okno.destroy()
        else:
            pass

okno = Tk()
okno.title("Klikacz")

przyciski =[]

for i in range(25):
    if i < 5:
        przycisk = Button(okno,width=10,text=str(unikalne_liczby[i]),command=(lambda x=i, p=str(unikalne_liczby[i]):klik(x,p)))
        przycisk.grid(row=i,column=0)
        przyciski.append(przycisk)
    elif i >= 5 and i < 10:
        przycisk = Button(okno,width=10,text=str(unikalne_liczby[i]),command=(lambda x=i, p=str(unikalne_liczby[i]):klik(x,p)))
        przycisk.grid(row=i-5,column=1)
        przyciski.append(przycisk)
    elif i >= 10 and i < 15:
        przycisk = Button(okno,width=10,text=str(unikalne_liczby[i]),command=(lambda x=i, p=str(unikalne_liczby[i]):klik(x,p)))
        przycisk.grid(row=i-10,column=2)
        przyciski.append(przycisk)
    elif i >= 15 and i < 20:
        przycisk = Button(okno,width=10,text=str(unikalne_liczby[i]),command=(lambda x=i, p=str(unikalne_liczby[i]):klik(x,p)))
        przycisk.grid(row=i-15,column=3)
        przyciski.append(przycisk)
    else:
        przycisk = Button(okno,width=10,text=str(unikalne_liczby[i]),command=(lambda x=i, p=str(unikalne_liczby[i]):klik(x,p)))
        przycisk.grid(row=i-20,column=5)
        przyciski.append(przycisk)

okno.mainloop()
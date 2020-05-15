from tkinter import *

from tkinter import messagebox



def tylkocyfry_1(*x):

    global liczba_1,pl_1

    s_1 = liczba_1.get()

    if s_1 == '' or s_1.isdigit():

        pl_1 = s_1

    else:

        liczba_1.set(pl_1)



def tylkocyfry_2(*y):

    global liczba_2,pl_2

    s_2 = liczba_2.get()

    if s_2 == '' or s_2.isdigit():

        pl_2 = s_2

    else:

        liczba_2.set(pl_2)



pl_1 = ''

pl_2 = ''



def poprawne_liczby():

    global r,pl_1,pl_2

    if pl_1 and pl_2 != '':

        pass

    else:

        messagebox.showinfo('Brak liczb','Podaj liczby')



def wyświetl_wynik():

    global r

    r_odp=r.get()

    if r_odp == 1:

        w = float(pl_1) + float(pl_2)

        messagebox.showinfo('Wynik dodawania',f'{pl_1} + {pl_2} = {w}')

    elif r_odp == 2:

        w = float(pl_1) - float(pl_2)

        messagebox.showinfo('Wynik dodawania',f'{pl_1} - {pl_2} = {w}')

    elif r_odp == 3:

        if pl_2 != '0':

            w = float(pl_1) / float(pl_2)

            messagebox.showinfo('Wynik dodawania',f'{pl_1} / {pl_2} = {w}')

        else:
            
            messagebox.showerror('ZeroDivisionError','Dzielenie przez zero jest niedozwolone')

    elif r_odp == 4:


        w = float(pl_1) * float(pl_2)

        messagebox.showinfo('Wynik dodawania',f'{pl_1} * {pl_2} = {w}')



okno = Tk()

okno.title("Kalkulatorek")

liczba_1 = StringVar()

liczba_2 = StringVar()

e1 = Entry(okno, textvariable = liczba_1)

e2 = Entry(okno, textvariable = liczba_2)

liczba_1.set(pl_1)

liczba_2.set(pl_2)

liczba_1.trace('w', tylkocyfry_1)

liczba_2.trace('w', tylkocyfry_2)

r= IntVar()

r1 = Radiobutton(okno, text="+", variable=r, value=1, command=poprawne_liczby)

r2 = Radiobutton(okno, text="-", variable=r, value=2, command=poprawne_liczby)

r3 = Radiobutton(okno, text="/", variable=r, value=3, command=poprawne_liczby)

r4 = Radiobutton(okno, text="*", variable=r, value=4, command=poprawne_liczby)

b = Button(okno, text="Oblicz", command=wyświetl_wynik)

e1.grid(row=0,column=0, rowspan=4)

r1.grid(row=0,column=1)

r2.grid(row=1,column=1)

r3.grid(row=2,column=1)

r4.grid(row=3,column=1)

b.grid(row=4,column=1)

e2.grid(row=0,column=2, rowspan=4)



okno.mainloop()


from tkinter import *

from tkinter import messagebox

from random import randint



PUSTE_POLE = " "

ILOSC_POL = 9

komputer = "X"

gracz = "O"



plansza = []

for pole in range(ILOSC_POL):

    plansza.append(PUSTE_POLE)



def wykonajKopiePlanszy():

    kopiaPlanszy = []

    for i in plansza:

        kopiaPlanszy.append(i)

    return kopiaPlanszy



def zwyciestwo():

    SPOSOBY_NA_WYGRANA = ((0, 1, 2),

                          (3, 4, 5),

                          (6, 7, 8),

                          (0, 3, 6),

                          (1, 4, 7),

                          (2, 5, 8),

                          (0, 4, 8),

                          (2, 4, 6))

    for w in SPOSOBY_NA_WYGRANA:

        if plansza[w[0]] == plansza[w[1]] == plansza[w[2]] != PUSTE_POLE:

            zwyciesca = plansza[w[0]]

            if zwyciesca == komputer:
                
                messagebox.showinfo('Zwycięstwo', 'Zwyciężył komputer')
            
            else:

                messagebox.showinfo('Zwycięstwo', 'Zwyciężył gracz')

            return zwyciesca

    if PUSTE_POLE not in plansza:

        messagebox.showinfo('Wynik!', 'Remis')

    return None



def wolne_pola():

    wp = []

    for pole in range(ILOSC_POL):

        if plansza[pole] == PUSTE_POLE:

            wp.append(pole)

    return wp





def komputer_AI():

    NAJLEPSZE_RUCHY = (4,0,2,6,8,1,3,5,7)

    plansza = wykonajKopiePlanszy()

    for ruch in wolne_pola():

        plansza[ruch] = komputer

        if zwyciestwo()  == komputer:

            return ruch

        plansza[ruch] = PUSTE_POLE

    for ruch in wolne_pola():       

        plansza[ruch] = gracz

        if zwyciestwo() == gracz:

            return ruch

        plansza[ruch] = PUSTE_POLE

    for ruch in NAJLEPSZE_RUCHY:

        if ruch in wolne_pola():

            return ruch



def wykonajRuch(x):

    global plansza

    if plansza[x] == PUSTE_POLE:

        przyciski[x]["text"] = gracz

        przyciski[x]["fg"] = "red"

        plansza[x] = gracz

        czyZwyciesca = zwyciestwo()

        if czyZwyciesca:

            return czyZwyciesca

        else:

            ruchKomputera()

    else:

        messagebox.showinfo('Pole zajęte', 'To pole jest zajęte')   



def ruchKomputera(e=None):

    ruch = komputer_AI()

    przyciski[ruch]["text"] = komputer

    przyciski[ruch]["fg"] = "green"

    plansza[ruch] = komputer

    czyZwyciesca = zwyciestwo()

    return czyZwyciesca

    

okno = Tk()

okno.title("OX")



przyciski = []



for i in range(9):

    if i < 3:

        przycisk = Button(okno, width=3, height=1, font=("Arial", "20", "bold"), command=(lambda x=i:wykonajRuch(x)))

        przycisk.grid(row=0,column=i)

        przyciski.append(przycisk)

    elif i >= 3 and i < 6:

        przycisk = Button(okno, width=3, height=1, font=("Arial", "20", "bold"), command=(lambda x=i:wykonajRuch(x)))

        przycisk.grid(row=1,column=i-3)

        przyciski.append(przycisk)

    else:

        przycisk = Button(okno, width=3, height=1, font=("Arial", "20", "bold"), command=(lambda x=i:wykonajRuch(x)))

        przycisk.grid(row=2,column=i-6)

        przyciski.append(przycisk)



start = przyciski[randint(0,8)]

start["text"] = komputer

start["fg"] = "green"

plansza[przyciski.index(start)] = komputer







okno.mainloop()


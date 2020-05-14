import tkinter as tk
from tkinter import messagebox



def czyPoprawny():
    pesel = user_pesel.get()
    PESEL = []
    NZNAKI = []
    if len(pesel) != 11:
        tk.messagebox.showinfo('Za krótki','PESEL powinien posiadać 11 cyfr. Podaj poprawny PESEL.')
    else:
        for i in pesel:
            if i.isdigit() == True:
                PESEL.append(int(i))
            else:
                NZNAKI.append(i)
        if len(NZNAKI) != 0:
            tk.messagebox.showinfo('Niedozwolone znaki','Użyłeś nieodpowiedniego znaku')
        else:
            suma = PESEL[0] + 3*PESEL[1] + 7*PESEL[2] + 9*PESEL[3] + PESEL[4] + 3*PESEL[5] + 7*PESEL[6] + 9*PESEL[7] + PESEL[8] + 3*PESEL[9] + PESEL[10]
            SUMA = list(str(suma))
            if int(SUMA[-1]) == 0:
                tk.messagebox.showinfo('Jest OK','Twój PESEL jest poprawny')
            else:
                tk.messagebox.showinfo('Nie jest OK','Twój PESEL jest niepoprawny')


o = tk.Tk()

user_pesel = tk.StringVar()

name_label = tk.Label(o, text="PESEL: ")
name_label.grid(row=0,column=0)
name_entry = tk.Entry(o, textvariable = user_pesel)
name_entry.grid(row=0,column=1)

pessel_button = tk.Button(o, text="Sprawdź!", command=czyPoprawny)
pessel_button.grid(row=1,column=0,columnspan=2)


o.mainloop()

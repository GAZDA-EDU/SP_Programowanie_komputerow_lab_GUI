from tkinter import *

osbt = ['0','0','0','0','0','0','0','0']

def zaznacz(x,p):
    global osbt
    if p.get() == 1:
        osbt[x] = '1'
    else:
        osbt[x] = '0'
    zb = ''.join(osbt)
    l['text'] = str(int(zb,2))


okno = Tk()
okno.title("Bitowiec")

c_buttons =[]

for i in range(8):
    przel=IntVar()
    c = Checkbutton(okno, text=str(i), variable=przel, command=(lambda x=i, p=przel:zaznacz(x,p)))
    c.grid(row=0,column=i)
    c_buttons.append(c)

l = Label(okno, text="0", font=("Arial", "50", "bold"), fg="blue")
l.grid(row=1,column=0,columnspan=8)

b = Button(okno, text="Koniec",command=okno.destroy)
b.grid(row=2,column=0,columnspan=8)

okno.mainloop()
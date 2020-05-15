from tkinter import *

okno = Tk()
okno.title("Żaglowiec")

#Płótno
c = Canvas(okno, width=400, height=400, bg='white')

#Kadłub
c.create_polygon(70,365,320,365,365,300,25,300, outline='#993366', fill='white')

#Bulaje
c.create_oval(310,350,280,320, outline='#993366', fill='white')
c.create_oval(265,350,235,320, outline='#993366', fill='white')

#Fokmaszt 
c.create_rectangle(225,300,235,20, outline='#993366', fill='white')
c.create_polygon(235,260,235,160,310,210, outline='#993366', fill='white')
c.create_polygon(235,160,235,60,310,110, outline='#993366', fill='white')

#Grotmaszt
c.create_line(80,230,200,230, fill='#993366')
c.create_line(80,110,200,110, fill='#993366')
c.create_rectangle(135,300,145,230, outline='#993366', fill='white')
c.create_rectangle(135,110,145,20, outline='#993366', fill='white')
c.create_arc(30,110,130,230, outline='#993366', style=ARC, start=270, extent=180)
c.create_arc(150,110,250,230, outline='#993366', style=ARC, start=90, extent=180)

#Koło sterowe
c.create_oval(60,285,90,255, width=2, outline='yellow', fill='white')
c.create_line(75,300,75,245, width=2, fill='yellow')
c.create_line(50,270,100,270, width=2, fill='yellow')
c.create_line(60,248,90,290, width=2, fill='yellow')
c.create_line(90,248,60,290, width=2, fill='yellow')

#Flaga
c.create_line(40,300,40,270, width=2, fill='red')
c.create_rectangle(40,270,10,278, outline='red', fill='white')
c.create_rectangle(40,278,10,286, outline='red', fill='red')

#Napis (SPPK - Studia Podyplomowe Programowanie Komputerów)
c.create_text(100,320,text="SPPK 2020",font=("Arial","12","bold"))

#Fale
for i in range(16):
    c.create_arc(i*30,365, (i+1)*30,380, style=ARC, start=15, extent=150,outline='blue')

c.grid(row=0)


okno.mainloop()
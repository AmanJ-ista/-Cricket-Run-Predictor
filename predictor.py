from tkinter import *
import tkinter
window=Tk()
from tkinter import messagebox
window.geometry('1000x1000')

top_frame=tkinter.Frame(window).pack(fill=BOTH,expand=True)
bottom_frame=tkinter.Frame(window).pack(side="bottom")

l1=Label(top_frame,text="CRICKET RUN PREDICTOR",bg="light blue",font=('calibre',40,'bold'))
l1.place(x=400,y=20)

var=StringVar()
var2=StringVar()

r1=Radiobutton(top_frame,text="One Day",value="One Day",variable=var,font = ('calibre',20,'bold'))
r1.select()
r1.place(x=600,y=150)


r2=Radiobutton(top_frame,text="T-20",value="T-20",variable=var,font = ('calibre',20,'bold'))
r2.place(x=900,y=150)



r3=Radiobutton(top_frame,text="Automatic",value="Automatic",variable=var2,font = ('calibre',20,'bold'))
r3.select()
r3.place(x=600,y=100)


r4=Radiobutton(top_frame,text="Manual",value="Manual",variable=var2,font = ('calibre',20,'bold'))
r4.place(x=900,y=100)


l2=Label(top_frame,text="Current Over",bg="light blue",font=('calibre',25,'bold'))
l2.place(x=450,y=200)

e1=Entry(top_frame,textvar='entry1',width=20,font=('Helvetica',20,'bold'))
e1.place(x=1000,y=200)

l3=Label(top_frame,text="Expected Score For Current Ball",bg="light blue",font=('calibre',25,'bold'))
l3.place(x=450,y=280)

e2=Entry(top_frame,textvar='entry2',width=20,font=('Helvetica',20,'bold'))
e2.place(x=1000,y=280)

l4=Label(top_frame,text="Expected Score After Match",bg="light blue",font=('calibre',25,'bold'))
l4.place(x=450,y=360)

e3=Entry(top_frame,textvar='entry3',width=20,font=('Helvetica',20,'bold'))
e3.place(x=1000,y=360)






from tkinter import *
from tkmacosx import Button
import time

def Play():
    wn.destroy()
    import main

wn = Tk()
wn.title('Save The Village')
wn.configure(bg='black')
wn.geometry('800x800')
Label(wn, text='SAVE THE VILLAGE', pady=50,font=('arial',50,'bold'),fg='white',bg='black').pack()
Button(wn, text='PLAY',bg='white',fg='black',padx=20,pady=20,command=Play).pack()
Button(wn, text='RATE',bg='white',fg='black',padx=20,pady=20).pack()
Button(wn, text='EXIT',bg='white',fg='black',padx=20,pady=20,command=wn.destroy).pack()
wn.mainloop()
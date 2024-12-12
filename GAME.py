from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic Tac Toe')
root.geometry('300x260')
root.config(bg='#333')
turn = 'X'
def Btnclk(b):
    if b['text']=='':
        global turn
        if turn == 'X':
            b['text'] = 'X'
            turn = 'O'
            com()
        else:
            b['text']='O'
            turn = 'X'
            com()
    else:
        messagebox.showerror('Redo','This place has been taken')
comb = []
def com():
    comb.clear()
    comb.append(b0['text']+b1['text']+b2['text'])
    comb.append(b0['text']+b3['text']+b6['text'])
    comb.append(b0['text']+b4['text']+b8['text'])
    comb.append(b1['text']+b4['text']+b7['text'])
    comb.append(b2['text']+b4['text']+b6['text'])
    comb.append(b2['text']+b5['text']+b8['text'])
    comb.append(b3['text']+b4['text']+b5['text'])
    comb.append(b6['text']+b7['text']+b8['text'])
    if 'XXX' in comb:
        messagebox.showinfo('Winner','X WON')
    elif 'OOO' in comb:
        messagebox.showinfo('Winner','O WON')
b0 = Button(root, text='', width=5,height=3,font=('Algerian',15),bg='white',fg='black',command=lambda:Btnclk(b0))
b1 = Button(root, text='', width=5,height=3,font=('Algerian',15),bg='white',fg='black',command=lambda:Btnclk(b1))
b2 = Button(root, text='', width=5,height=3,font=('Algerian',15),bg='white',fg='black',command=lambda:Btnclk(b2))
b3 = Button(root, text='', width=5,height=3,font=('Algerian',15),bg='white',fg='black',command=lambda:Btnclk(b3))
b4 = Button(root, text='', width=5,height=3,font=('Algerian',15),bg='white',fg='black',command=lambda:Btnclk(b4))
b5 = Button(root, text='', width=5,height=3,font=('Algerian',15),bg='white',fg='black',command=lambda:Btnclk(b5))
b6 = Button(root, text='', width=5,height=3,font=('Algerian',15),bg='white',fg='black',command=lambda:Btnclk(b6))
b7 = Button(root, text='', width=5,height=3,font=('Algerian',15),bg='white',fg='black',command=lambda:Btnclk(b7))
b8 = Button(root, text='', width=5,height=3,font=('Algerian',15),bg='white',fg='black',command=lambda:Btnclk(b8))
b0.grid(row=0,column=0,padx=10,pady=10)
b1.grid(row=0,column=1,padx=10,pady=10)
b2.grid(row=0,column=2,padx=10,pady=10)
b3.grid(row=1,column=0,padx=10,pady=10)
b4.grid(row=1,column=1,padx=10,pady=10)
b5.grid(row=1,column=2,padx=10,pady=10)
b6.grid(row=2,column=0,padx=10,pady=10)
b7.grid(row=2,column=1,padx=10,pady=10)
b8.grid(row=2,column=2,padx=10,pady=10)
root.mainloop() #very important

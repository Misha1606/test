from tkinter import *
from tkinter import messagebox

def button_1():
    messagebox.showinfo('Результат', int(entry.get())+int(entry1.get()))

def button_2():
    messagebox.showinfo('Результат', int(entry.get()) - int(entry1.get()))

def button_3():
    messagebox.showinfo('Результат', int(entry.get()) * int(entry1.get()))


def button_4():
    messagebox.showinfo('Результат', int(entry.get()) / int(entry1.get()))


def button_5():
    messagebox.showinfo('Результат', int(entry.get()) // int(entry1.get()))


def button_6():
    messagebox.showinfo('Остаток', int(entry.get()) % int(entry1.get()))
root=Tk()
root.title('Приложение')
root.geometry('500x300')

entry = Entry(root, width=10,  bg='gray', fg='cyan', font='consolas')
entry.pack()
entry1 = Entry(root, width=10,  bg='gray', fg='cyan', font='consolas')
entry1.pack()

Button(root, text='+', width=10, height=2, bg='cyan', command=button_1).pack()
Button(root, text='-', width=10, height=2, bg='cyan', command=button_2).pack()
Button(root, text='*', width=10, height=2, bg='cyan', command=button_3).pack()
Button(root, text='/', width=10, height=2, bg='cyan', command=button_4).pack()
Button(root, text='//', width=10, height=2, bg='cyan', command=button_5).pack()
Button(root, text='%', width=10, height=2, bg='cyan', command=button_6).pack()

root.mainloop()
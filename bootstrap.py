from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

my_w = ttk.Window(themename="superhero")
my_w.title("Hello")
my_w.geometry("500x250") # width and height of the window 



b1 = ttk.Button(my_w, text="Button Success", bootstyle=SUCCESS).grid(row=0, column=0, padx=30, pady=10)

b1 = ttk.Button(my_w, text="Button Primary", bootstyle=PRIMARY).grid(row=0, column=1, padx=30, pady=10)

my_txt = ttk.Label(my_w, text='Abi dabaya nahi hai', font=("Helvetica 20 bold"), bootstyle ='primary').grid(row=1)

def checker():
    if var.get() == 1:
        my_txt.config(text='Dabadiya')
    else:
        my_txt.config(text='Abe Dabana')
var = IntVar()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
check = ttk.Checkbutton(text='Teri marzi dabade', bootstyle= "success", variable=var, onvalue=1, offvalue=0, command=checker).grid(row=2)
check = ttk.Checkbutton(text='Teri marzi dabade', bootstyle= "success toolbutton", variable=var, onvalue=1, offvalue=0, command=checker).grid(row=6)
check = ttk.Radiobutton(text='Teri marzi dabade', bootstyle= "success", variable=var1, command=checker).grid(row=3)
check = ttk.Checkbutton(text='', bootstyle= "success round-toggle", variable=var2).grid(row=0, column=4)
check = ttk.Checkbutton(text='Teri marzi dabade', bootstyle= "success square-toggle", variable=var3, command=checker).grid(row=5)

my_w.mainloop()
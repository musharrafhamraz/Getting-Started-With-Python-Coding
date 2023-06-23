from tkinter import *
import ttkbootstrap as ttk

 
var = 'darkly'

root = ttk.Window(themename=var)
root.geometry('600x600')
root.title('Theme Change')

def change():
    if var1.get() == 1:
        var = 'darkly',
        print('done')
    else:
        var = 'superhero'
        print('done')
    return var

my_label = ttk.Label(text='Theme Changer', font=('Helvetica 13 bold'), bootstyle="primary").grid(row=0, column=0, padx = 12, pady= 12)

var1 = IntVar()
my_toggle = ttk.Checkbutton(text="", bootstyle= 'success round-toggle',variable=var1, command=change).grid(row=0, column=3, padx = 12, pady= 12)
root.mainloop()
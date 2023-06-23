from tkinter import *
import ttkbootstrap as tk
root = tk.Window(themename="darkly")
root.geometry("500x500")

def myfunc():
    pass

yourmenu = tk.Menu(root)

m1 = tk.Menu(yourmenu, tearoff=0, background="#fff")
m2 = tk.Menu(yourmenu,tearoff = 0)
m3 = tk.Menu(yourmenu,tearoff = 0)
m4 = tk.Menu(yourmenu,tearoff = 0)

yourmenu.add_cascade(label="File",menu=m1)
yourmenu.add_cascade(label="View",menu=m2)
yourmenu.add_cascade(label="Help",menu=m3)
yourmenu.add_cascade(label="Run",menu=m4)


m1.add_cascade(label="New Project", command=myfunc)
m1.add_cascade(label="Save", command=myfunc)
m1.add_cascade(label="Log Out", command=myfunc)
m1.add_separator()
m1.add_cascade(label="Save", command=myfunc)
m1.add_cascade(label="Save As", command=myfunc)


m2.add_cascade(label="Thumbnail", command=myfunc)
m2.add_cascade(label="Hide Advance", command=myfunc)


m4.add_cascade(label="Start Debugging          F5", command=myfunc)
m4.add_cascade(label="Hide Advance", command=myfunc)



m3.add_cascade(label="Press F1", command=myfunc)
m3.add_cascade(label="Advance Help", command=myfunc)


root.config(menu = yourmenu)





root.mainloop()
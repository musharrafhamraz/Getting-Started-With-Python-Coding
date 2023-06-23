from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Hello")
root.geometry("600x600")


var = Label(text="Hello My name is Musharraf", bg="grey", fg="white", font=("comicsnas 19 bold"), padx=23, pady=23).pack(pady=40)
image = Image.open("pic2.png")
image = image.resize((300, 300), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)
varun_label = Label(image=photo)
varun_label.pack()


root.mainloop()





#  image = Image.open(f"{i+1}.png")
#     #TODO: Resize these images
#     image = image.resize((225, 265), Image.ANTIALIAS)
#     photos.append(ImageTk.PhotoImage(image))
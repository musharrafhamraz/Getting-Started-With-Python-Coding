from tkinter import *
from PIL import Image, ImageTk
import pymongo
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# def store_values():
#     with open("info.txt", "a") as f:
#         f.write("\n\n")
#         f.write(f"Customer Name: {fullname_value.get()}\n")
#         f.write(f"Customer username: {username_value.get()}\n")
#         f.write(f"Customer Age: {age_value.get()}\n")
#         f.write(f"Customer password: {password_value.get()}\n")
#         f.write(f"Customer Service: {foodservice_value.get()}\n")

# def create_database():
#     global client
#     global collection
#     client = pymongo.MongoClient('mongodb://localhost:27017')
#     db = client['ShopInformation']
#     collection = db['CustomerInfo']

client = pymongo.MongoClient('mongodb://localhost:27017')
print(client)
db = client['ShopInformation']
collection = db['CustomerInfo']


def add_data():
    dictionary = {
        'Customer_Name': f'{fullname_value.get()}',
        'Items_Sold': f'{username_value.get()}',
        'Items_Cost': f'{age_value.get()}',
        'Accessries': f'{password_value.get()}'
    }
    collection.insert_one(dictionary)


def display_data():
    global data

    data = collection.find()
    tree = ttk.Treeview(profile, columns=('Items_Sold', 'Items_Cost', 'Accessries'), show='headings')
    tree.heading('#1', text='Customer Name')
    tree.heading('#2', text='Items Sold')
    tree.heading('#3', text='Items Cost')
    for document in data:
        tree.insert('', 'end', values=(document['Customer_Name'], document['Items_Sold'], document['Items_Cost'], document['Accessries']))
        tree.grid(row=9, column=2, rowspan=4, sticky='nsew')
        scroll = ttk.Scrollbar(profile, orient='vertical', command=tree.yview)
        scroll.grid(row=9, column=3, rowspan=4, sticky='ns')
        tree.configure(yscrollcommand=scroll.set)

def update_data():
    pass


def delete_data():
    pass


def validate_number(x):
    """Validates that the input is a number"""
    if x.isdigit():
        return True
    elif x == "":
        return True
    else:
        return False


def validate_alpha(x):
    """Validates that the input is alpha"""
    if x.isdigit():
        return False
    elif x == "":
        return True
    else:
        return True


def profile_screen():
    global profile
    profile = Toplevel(root)

    profile.title("Profile Description")
    profile.geometry("800x800")


    ttk.Label(profile, text="Information", font="Oswald 20 bold").grid(
        row=0, column=1, sticky=E + W)

    ttk.Button(profile, text="Refresh",
               command=update_data).grid(row=13, column=1)


root = ttk.Window(themename="superhero")
root.geometry('700x600')
root.minsize(700, 600)
root.maxsize(700, 600)
root.title('Khate Ki Software')
digit_func = root.register(validate_number)
alpha_func = root.register(validate_alpha)
heading = ttk.Label(root, text='Welcome to Traders',
                    font=('Georgia 24 bold')).grid(row=0, column=2)

fullname = ttk.Label(root, text='Customer Name').grid(row=1, column=1)
username = ttk.Label(root, text='Items Sold').grid(row=2, column=1)
age = ttk.Label(root, text="Item Cost").grid(row=3, column=1)
password = ttk.Label(root, text="Accesseries").grid(row=4, column=1)



fullname_value = StringVar()
username_value = StringVar()
age_value = StringVar()
password_value = StringVar()
c_password_value = StringVar()
foodservice_value = IntVar()


fullname_entry = ttk.Entry(
    root, textvariable=fullname_value, validate='focus', validatecommand=(alpha_func, '%P')).grid(row=1, column=2)
username_entry = ttk.Entry(
    root, textvariable=username_value, validate='focus', validatecommand=(alpha_func, '%P')).grid(row=2, column=2)
age_entry = ttk.Entry(root, textvariable=age_value, validate='focus',
                      validatecommand=(digit_func, '%P')).grid(row=3, column=2)
password_entry = ttk.Entry(
    root, textvariable=password_value,).grid(row=4, column=2)


ttk.Label(text=" ").grid(row=6, column=2)

service = ttk.Checkbutton(text='Do You Want the Delivery Service',
                          variable=foodservice_value).grid(row=7, column=2)


btn = ttk.Button(text="Add Data",
                 command=add_data,).grid(row=9, column=2, pady=9)
btn1 = ttk.Button(text="Show Details", command=lambda: (
    profile_screen(), display_data()),).grid(row=11, column=2, pady=9)

# image = Image.open("shop.png")
# image = image.resize((300, 300), Image.LANCZOS)
# photo = ImageTk.PhotoImage(image)
# thanks = Label(image=photo).grid(row=12, column=2)


root.mainloop()

from tkinter import *
import pymongo

def add_data():
    client = pymongo.MongoClient('mongodb://localhost:27017')
    print(client)
    db = client['AppData']
    collection = db['UserInfo']
    dictionary = {
        # 'Customer_Name':f'{fullname_value.get()}',
        # 'Customer_username': f'{username_value.get()}',
        # 'Customer_Age': f'{username_value.get()}',
        # 'Customer_password': f'{username_value.get()}'
    }
    add = collection.insert_one(dictionary)

    return add

def display_data():
    pass

def update_data():
    pass

def delete_data():
    pass


def register():
    screen1=Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("400x400")

    Label(screen1,text="Please Enter Details below", bg="grey",width="600", height="2", font=("helvetica", 13, "bold")).pack()
    Label(screen1,text='').pack()
    fullname = StringVar()
    password = StringVar()
    username = StringVar()
    c_password = StringVar()
    Label(screen1,text='Full Name*').pack()
    fullname1= Entry(screen1,textvariable=fullname).pack()
    Label(screen1,text='Username*').pack()
    username1=Entry(screen1,textvariable=username).pack()
    Label(screen1,text='Password*').pack()
    password1=Entry(screen1,textvariable=password).pack()
    Label(screen1,text='Confirmed Password*').pack()
    c_password1=Entry(screen1,textvariable=c_password).pack()
    Label(screen1,text='').pack()
    Button(screen1,text='Register', height="2", width='30',font=("helvetica", 13, "bold"), command=login).pack()

    
def login():
    screen2=Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("400x400")

    Label(screen2,text="Please Enter Details below", bg="grey",width="600", height="2", font=("helvetica", 13, "bold")).pack()
    Label(screen2,text='').pack()
    password = StringVar()
    username = StringVar()
    Label(screen2,text='Username*').pack()
    Entry(screen2,textvariable=username).pack()
    Label(screen2,text='Password*').pack()
    Entry(screen2,textvariable=password).pack()
    Label(screen2,text='').pack()
    Button(screen2,text='Login', height="2", width='30',font=("helvetica", 13, "bold"), command=login).pack()


def main_screen():
    global screen
    screen=Tk()
    screen.geometry("600x600")
    screen.title("Web App")

    Label(text='Web App', bg="grey",width="600", height="2", font=("helvetica", 13, "bold")).pack()
    Label(text='').pack()
    Button(text='Login', height="2", width='30',font=("helvetica", 13, "bold"), command=login).pack()
    Label(text='').pack()
    Button(text='Register', height="2", width='30',font=("helvetica", 13, "bold"), command=register).pack()

    screen.mainloop()

main_screen()
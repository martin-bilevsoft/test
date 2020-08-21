from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from tkinter import *
from PIL import ImageTk, Image

width = 350
height = 500

root = Tk()
root.geometry(f'{width}x{height}')


entryUsername = Entry(root, width=25, borderwidth=2)
entryUsername.place(x=0, y=0)
entryUsername.insert(0, "Username")
username = ""


entryPassword = Entry(root, width=25, borderwidth=2, show="*")
entryPassword.place(x=0, y=35)
entryPassword.insert(0, "Password")
password = ""


def secondWindow():
    root.destroy()
    root1 = Tk()

    load = Image.open("f8.jpg")
    image1 = ImageTk.PhotoImage(load)

    width, height = load.size
    root1.geometry(f'{width}x{height}')

    label = Label(root1, image = image1).pack()
    label.image = image1
    label = Label(root, text="Hello")
    label.place(x=10, y=10)

    #label = Label(root1, text= "Hello", bg="green", fg="white")
    #label.config(font=(16))
    #label.pack(ipadx=75, pady=70)


def checkLoginInfo(username, password):
    if username == "123" and password == "123":
        secondWindow()


    else:
        label = Label(root, text= "Incorrect username/password", bg="red", fg="white")
        label.config(font=(16))
        label.pack(pady=70)


def getLoginInfo():
    username = entryUsername.get()
    password = entryPassword.get()

    entryUsername.configure(state='disabled')
    entryPassword.configure(state='disabled')
    buttonEnter.configure(state='disabled')

    checkLoginInfo(username, password)


buttonEnter = Button(root, text="Enter", command=getLoginInfo)
buttonEnter.place(x=width-50, y = 35)

root.mainloop()
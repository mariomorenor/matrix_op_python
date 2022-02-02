from tkinter import *
from tkinter import messagebox
import Main as MainWindow

def init():
    global loginWindow
    global username
    global password

    loginWindow = Tk()
    loginWindow.title("Login")
    loginWindow.geometry("300x170")
    
    
    Label(text="Usuario").pack()

    username = StringVar()
    Entry(textvariable=username).pack()
    Label(text="Contraseña").pack()

    password = StringVar()
    Entry(textvariable=password).pack()
    Button(text="Ingresar", command=login, width=20).pack(pady=10)
    
    loginWindow.mainloop()

def login():
    if username.get() == "admin" and password.get() == "admin":
        loginWindow.destroy()
        MainWindow.init()
    else:
        messagebox.showerror(title="Ocurrió un Error",message="Verifique sus credenciales")
    

init()

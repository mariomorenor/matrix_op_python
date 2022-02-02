from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview


import login as loginWindow
import filtros as Filtros

trvColumns = ("account","event_code","date","description")

def init():
    global mainWindow
    global trvSeniales

    mainWindow = Tk()
    mainWindow.geometry("1200x600")
    mainWindow.title("Matrix Operator")

    # Container

    # Menubar
    menubar = Menu(mainWindow)
    mainWindow.config(menu=menubar)
    
    # Menú Archivo
    mbArchivo = Menu(menubar, tearoff=0)
    mbArchivo.add_separator()
    mbArchivo.add_cascade(label="Cerrar Sesión", command=logout)

    # Menú Filtros
    mbDatos = Menu(menubar, tearoff=0)
    mbDatos.add_cascade(label="Filtros",command=showFiltrosWindow)

    # Menú Principal
    menubar.add_cascade(label="Archivo", menu=mbArchivo)
    menubar.add_cascade(label="Datos", menu=mbDatos)


    # TreeView
    trvSeniales = Treeview(mainWindow,columns=trvColumns)
    trvSeniales.heading("#0",text="Estado")
    trvSeniales.heading("account",text="Cuenta")
    trvSeniales.heading("event_code",text="Cód.Event.")
    trvSeniales.heading("date",text="Fecha")
    trvSeniales.heading("description",text="Descripción")

    trvSeniales.grid(row=0,column=0)

    mainWindow.mainloop()



def logout():
    res = messagebox.askyesno(title="Cerrando Sesión",message="¿Está Seguro de Salir?")
    if res:
        mainWindow.destroy()
        loginWindow.init()

def showFiltrosWindow():
    
    filtrosWindow = Filtros.init(parentWin=mainWindow)


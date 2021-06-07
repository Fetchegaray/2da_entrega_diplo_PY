"""
Programa principal. Se encarga de la interface grafica, genera la ventana y maneja el tree.

"""

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from clase_db import Basedatos


db = Basedatos()
"""
Se instancia la clase de manejo de la base de datos

"""


def selecionarclick(event):
    """
    Funcion para detectar el click en el objeto del tree

    """
    item = tree.identify('item', event.x, event.y)
    myId.set(tree.item(item, "text"))
    myname.set(tree.item(item, "values")[0])
    myaddress.set(tree.item(item, "values")[1])
    mydateofbirth.set(tree.item(item, "values")[2])
    myemail.set(tree.item(item, "values")[3])
    mycity.set(tree.item(item, "values")[4])


def limpiar_campos():
    """
    Funcion para limpiar los campos de texto

    """
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)


def mensaje():
    """
    Mensaje personalizado para el menu "Acerca de"

    """
    acerca = "Aplicación Grafica con database SQlite3 Version 1.0 Tegnología Python Tkinter"
    messagebox.showinfo(title="INFORMACION", message=acerca)


def cargar_tk():
    """
    Funcion para generar la tupla con los datos y pasarsela a la clase del CRUD para crear una fila

    """
    tup_tk = myname.get(), myaddress.get(
    ), mydateofbirth.get(), myemail.get(), mycity.get()
    db.cargar(tup_tk)
    mostrar_tk()


def actualiza_tk():
    """
    Funcion para generar la tupla con los datos y pasarsela a la clase del CRUD para actualizar una fila

    """
    tup_tk = myname.get(), myaddress.get(
    ), mydateofbirth.get(), myemail.get(), mycity.get()
    id = myId.get()
    db.actualizar(tup_tk, id)
    mostrar_tk()


def mostrar_tk():
    """
    Funcion para mostrar los datos en el Tree y trarlos con la clase del CRUD

    """
    registros = tree.get_children()
    for elemento in registros:
        tree.delete(elemento)
    try:
        db.mostrar()
        for n in db.tup_db:
            tree.insert("", 0, text=n[0], values=(
                n[1], n[2], n[3], n[4], n[5]))
    except Exception as e:
        print(e, "error")


raiz = Tk()
raiz.title(
    "Campaña vacunación contra el Covid-19 | Ingresar a los nuevos inscriptos")
raiz.geometry("1100x350")
raiz.resizable(False, False)
myId = StringVar()
myname = StringVar()
myaddress = StringVar()
mydateofbirth = StringVar()
myemail = StringVar()
mycity = StringVar()
tree = ttk.Treeview
"""
Configuracion de la ventana

"""

menubar = Menu(raiz)
raiz.config(menu=menubar)
menubasedat = Menu(menubar, tearoff=0)
menubasedat.add_command(
    label="Crear / Conectar base de datos", command=lambda: db.crear())
menubasedat.add_command(
    label="Eliminar base de datos", command=lambda: [db.eliminar(), db.crear(), mostrar_tk()])
menubasedat.add_command(label="Salir", command=lambda: raiz.destroy())
menubar.add_cascade(label="Inicio", menu=menubasedat)
"""
Menu Inicio

"""

ayudamenu = Menu(menubar, tearoff=0)
ayudamenu.add_command(label="Resetear Campos",
                      command=lambda: limpiar_campos())
ayudamenu.add_command(
    label="Acerca", command=lambda: mensaje())
menubar.add_cascade(label="Ayuda", menu=ayudamenu)
raiz.config(menu=menubar)
"""
Menu Ayuda

"""

e1 = Entry(raiz, textvariable=myId)

l2 = Label(raiz, text="Nombre completo")
l2.grid(row=0, column=0)
e2 = Entry(raiz, textvariable=myname, width=25)
e2.focus()
e2.grid(row=0, column=1)

l3 = Label(raiz, text="Domicilio")
l3.grid(row=1, column=0)
e3 = Entry(raiz, textvariable=myaddress, width=25)
e3.grid(row=1, column=1)

l4 = Label(raiz, text="Fecha de nacimiento")
l4.grid(row=0, column=2)
e4 = Entry(raiz, textvariable=mydateofbirth, width=25)
e4.grid(row=0, column=3)

l5 = Label(raiz, text="Correo electrónico")
l5.grid(row=1, column=2)
e5 = Entry(raiz, textvariable=myemail, width=30)
e5.grid(row=1, column=3)

l6 = Label(raiz, text="Lugar de recidencia actual")
l6.grid(row=0, column=4)
e6 = Entry(raiz, textvariable=mycity, width=25)
e6.grid(row=0, column=5)
"""
Creación de las etiquetas y cajas de texto

"""

b1 = Button(raiz, text="Cargar Registro",
            command=lambda: [cargar_tk(), limpiar_campos()])
b1.place(x=50, y=90)
b2 = Button(raiz, text="Modificar Registro",
            command=lambda: [actualiza_tk(), limpiar_campos()])
b2.place(x=180, y=90)
b3 = Button(raiz, text="Mostrar Lista",
            command=lambda: mostrar_tk())
b3.place(x=320, y=90)
b4 = Button(raiz, text="Eliminar Registro",
            command=lambda: [db.borrar(myId.get()), mostrar_tk(), limpiar_campos()])
b4.place(x=450, y=90)
"""
Creación de los botones

"""

tree = ttk.Treeview(height=10, columns=(
    '#0', '#1', '#2', '#3', '#4', '#5'))
tree.place(x=0, y=130)
tree.column('#0', width=100)
tree.heading('#0', text="ID", anchor=CENTER)
tree.heading('#1', text="Nombre completo", anchor=CENTER)
tree.heading('#2', text="Domicilio", anchor=CENTER)
tree.heading('#3', text="Fecha de nacimiento", anchor=CENTER)
tree.heading('#4', text="Correo electrónico", anchor=CENTER)
tree.heading('#5', text="Lugar de recidencia actual", anchor=CENTER)
"""
Configura el tree

"""
tree.bind("<Double-1>", selecionarclick)


raiz.mainloop()

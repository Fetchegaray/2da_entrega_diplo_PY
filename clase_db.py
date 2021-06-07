""" 
Clase que se encarga de manejar el CRUD de la DB, tambien hereda los metodos de la clase de
validacion con Regex para poder validar antes de agregar o modificar una entrada 

"""

import sqlite3
from tkinter import messagebox
from clase_regex import Reg


class Basedatos(Reg):

    def __int__(self, tup_db):
        print("La clase hace el manejo de la base de datos")
        self.tup_db = tup_db

    def crear(self):
        """ 
        Crea la base de datos

        """
        myconecction = sqlite3.connect("base.db")
        mycursor = myconecction.cursor()
        try:
            mycursor.execute('''
            CREATE TABLE registro (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(50) NOT NULL,
            DOMICILIO VARCHAR(50) NOT NULL,
            FECHANAC VARCHAR(50) NOT NULL,
            CORREOELEC VARCHAR(50) NOT NULL,
            LUGARR VARCHAR(50) NOT NULL)
            ''')
            messagebox.showinfo(title="INFORMACION",
                                message="Se ha creado la base de datos")
        except:
            messagebox.showinfo(
                title="INFORMACION", message="La base ya estaba creada o hubo un error al crearla")

    def eliminar(self):
        """ 
        Elimina la tabla de la base 

        """
        try:
            myconecction = sqlite3.connect("base.db")
            mycursor = myconecction.cursor()
            mycursor.execute("DROP TABLE registro")
            messagebox.showinfo(title="INFORMACION", message="Base Borrada")
        except:
            messagebox.showinfo(
                title="ERROR", message="Error al borrar la base")

    def cargar(self, tupdat):
        """
        Carga los valores a la tabla que se le pasa por la tupla, tiene que tener 5 valores. Al mismo tiempo
        llama a los metodos de la clase de validacion de campos. Si no valida, no los carga.

        """
        verif = Reg()
        myconecction = sqlite3.connect("base.db")
        mycursor = myconecction.cursor()
        try:
            verif.veriftxt(tupdat)
            verif.veriffecha(tupdat)
            verif.verifmail(tupdat)
            verif.verifdir(tupdat)
            mycursor.execute(
                "INSERT INTO registro VALUES(NULL,?,?,?,?,?)", (tupdat))
            myconecction.commit()
        except:
            pass

    def mostrar(self):
        """ 
        Muestra la tabla completa de la base 

        """
        global tup_db
        myconecction = sqlite3.connect("base.db")
        mycursor = myconecction.cursor()
        try:
            mycursor.execute("SELECT * FROM registro")
            mostrar_val = mycursor.fetchall()
            self.tup_db = tuple(row for row in mostrar_val)
            if self.tup_db == ():
                raise Exception("error")
        except:
            messagebox.showinfo(
                title="ERROR", message="Error al mostrar el contenido de la base de datos")

    def actualizar(self, tupdat, iidd):
        """
        Actualiza los valores para una fila en particular, hay que pasarle una tupla con 5 posiciones
        con los datos y un string con el ID de la fila deseada
        Al mismo tiempo llama a los metodos de la clase de validacion de campos. Si no valida, no actualiza. 

        """
        verif = Reg()
        myconecction = sqlite3.connect("base.db")
        mycursor = myconecction.cursor()
        try:
            verif.veriftxt(tupdat)
            verif.veriffecha(tupdat)
            verif.verifmail(tupdat)
            verif.verifdir(tupdat)
            mycursor.execute("UPDATE registro SET NOMBRE= ?, DOMICILIO= ?, FECHANAC= ?, CORREOELEC= ?, LUGARR= ? WHERE ID= ?",
                             (tupdat[0], tupdat[1], tupdat[2], tupdat[3], tupdat[4], iidd))
            myconecction.commit()
        except:
            pass

    def borrar(self, iidd):
        """ 
        Borra una fila en particular, hay que pasarle el ID de la fila deseada 

        """
        myconecction = sqlite3.connect("base.db")
        mycursor = myconecction.cursor()
        try:
            mycursor.execute("DELETE FROM registro WHERE ID="+iidd)
            myconecction.commit()
        except:
            messagebox.showinfo(
                title="ERROR", message="Error al borrar el registro")


if __name__ == "__main__":
    db = Basedatos()
    db.mostrar()
    print(db.tup_db)
    db.crear()
    print("Los datos se perderan definitivamente ¿desea continuar de todos modos? (S / N)")
    pregunta = input()
    if (pregunta == "S") or (pregunta == "s"):
        db.eliminar()
        print("Base borrada")
    else:
        print("Base no borrada")
    tupdat_ext = ("fer", "Direccion", "29/04/2021",
                  "correo@mail.com", "Lugar de residencia")
    db.cargar(tupdat_ext)
    db.mostrar()
    tupdat_ext = ("feractualiz", "Direccion", "29/04/2021",
                  "correo@mail.com", "Lugar de residencia")
    iidd_ext = "16"
    db.actualizar(tupdat_ext, iidd_ext)
    iidd_ext = "4"
    print("¿Realmente desea eliminar el registro?", iidd_ext)
    pregunta = input()
    if (pregunta == "S") or (pregunta == "s"):
        db.borrar(iidd_ext)
        print("Entrada borrada")
    else:
        print("Entrada no borrada")

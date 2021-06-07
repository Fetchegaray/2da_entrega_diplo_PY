"""
Clase con los metodos de validacion de cada uno de los tipos de datos que se manejan en la 
aplicacion, texto, numeros, fechas, correo electronico y ningun campo vacio

"""

import re
from tkinter import messagebox


class Reg():

    def __int__(self,):
        print("La clase hace el manejo de la la verificacion de lo ingresado en los campos")

    def veriftxt(self, tupdatreg):
        """
        Verifica que los campos Nombre y Ciudad tengan solo letras

        """
        cond = True
        reg = re.compile(r"^[A-Za-z.-]+(\s*[A-Za-z.-]+)*$")
        if reg.match(tupdatreg[0]) and reg.match(tupdatreg[4]) is not None:
            #print(tupdatreg, "los campos 0 y 4 son validos")
            pass
        else:
            cond = False
            messagebox.showinfo(
                title="ERROR", message="Los campos Nombre y Lugar de residencia solo pueden contener letras y no estar vacios")
            # print(
            # "Los campos Nombre y Lugar de residencia solo pueden contener letras y no estar vacios")
        assert cond == True

    def veriffecha(self, tupdatreg):
        """
        Verifica que lo ingresado sea una fecha valida con el formato DD/MM/AAAA

        """
        cond = True
        reg = re.compile(
            r"^(0[1-9]|[1-2][0-9]|3[0-1])\/(0[1-9]|1[0-2])\/(\d{4})$")
        if reg.match(tupdatreg[2]) is not None:
            #print(tupdatreg, "el campo 2 es valido")
            pass
        else:
            cond = False
            messagebox.showinfo(
                title="ERROR", message="El campo fecha de nacimiento solo acepta formato DD/MM/AAAA")
            #print("El campo fecha de nacimiento solo acepta formato DD/MM/AAAA")
        assert cond == True

    def verifmail(self, tupdatreg):
        """
        Verifica que lo ingresado en el campo sea una direccion de correo valida con la forma
        direccion@servidor.com

        """
        cond = True
        reg = re.compile(
            r"^((\w[^\W]+)[\.\-]?){1,}\@(([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$")
        if reg.match(tupdatreg[3]) is not None:
            #print(tupdatreg, "el campo 3 es valido")
            pass
        else:
            cond = False
            messagebox.showinfo(
                title="ERROR", message="El campo E-mail es debe tener la forma mail@servidor.com")
            #print("El campo E-mail es debe tener la forma mail@servidor.com")
        assert cond == True

    def verifdir(self, tupdatreg):
        """
        Verifica que el campo Direccion no este vacio

        """
        cond = True
        if tupdatreg[1] != "":
            #print(tupdatreg, "el campo 1 es valido")
            pass
        else:
            cond = False
            messagebox.showinfo(
                title="ERROR", message="El campo Direccion no puede estar vacio")
        assert cond == True


if __name__ == "__main__":
    validar = Reg()
    tupdatreg_ext = ("Direccion", "fewsfd", "29/04/2021",
                     "correo@mail.com", "Lugar de residencia")
    validar.veriftxt(tupdatreg_ext)
    validar.veriffecha(tupdatreg_ext)
    validar.verifdir(tupdatreg_ext)
    validar.verifmail(tupdatreg_ext)

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror

import string

#Configuración del alfabeto
alfabeto = string.ascii_lowercase + string.ascii_lowercase

# Variables
#texto_input = "Prueba de oracion"
num_clave = 10

def cifrar(texto, clave):
    output = ""
    for letra in texto:

        x = ord(letra)

        if x == ord(" "):
            output+= " "
        else:
            output+= chr(x+clave)

    return output


def descifrar(texto,clave):
    output = ""
    for letra in texto:

        x = ord(letra)

        if x == ord(" "):
            output+= " "
        else:
            output+= chr(x-clave)

    return output



#INTERFAZ
root = Tk()
frm = ttk.Frame(root, padding=20)
root.geometry('600x300')
root.title("TF")

frm.grid()

ttk.Label(frm, text="Ingrese Texto:").grid(column=0, row=0)
ttk.Label(frm, text="Texto Encriptado: ").grid(column=0, row=4,pady=10)
ttk.Label(frm, text="Texto Desencriptado: ").grid(column=0, row=7,pady=10)

ttk.Button(frm, text="Salir", command=root.destroy).grid(column=2, row=15,pady=10)
#INPUTS
encry = StringVar()
encrybox = ttk.Entry(frm, textvariable=encry)
encrybox.grid(column=0, row=1)

key = StringVar()
key = ttk.Entry(frm, textvariable=key)
key.grid(column=0, row=10)

decry = StringVar()
decrybox = ttk.Entry(frm, textvariable=decry)
decrybox.grid(row=5, column=0)

def clave():
    num_clave=key.get()
    return num_clave
    

def encriptado():
    try:
        num_clave=int(key.get())
        
        texto_input=encry.get()
        texto_cifrado = cifrar(texto_input,num_clave)
        print(texto_cifrado)
        print(descifrar(texto_cifrado,num_clave))
        result =  texto_cifrado 
        Fresult_label.config(text=result)
    except ValueError as error:
        showerror(title='Error', message=error)


def desencriptado():
    try:
        num_clave=int(key.get())
        texto_cifrado=decry.get()
        texto_descifrado = descifrar(texto_cifrado,num_clave)
        print(texto_cifrado)
        print(descifrar(texto_cifrado,num_clave))
        result = texto_descifrado 
        Sresult_label.config(text=result)
    except ValueError as error:
        showerror(title='Error', message=error)

#LIMPIAR TEXTO
def ClearText():
    encrybox.delete(0,END)
    decrybox.delete(0,END)
    Fresult_label.config(text="")
    Sresult_label.config(text="")

#BOTONES LLAMAN A FUNCION
encriptBut=ttk.Button(frm,text="Encriptar")
encriptBut.grid(column=2,row=1)
encriptBut.configure(command=encriptado)

desencriptBut=ttk.Button(frm,text="Desencriptar")
desencriptBut.grid(column=2,row=5)
desencriptBut.configure(command=desencriptado)

cla=ttk.Button(frm,text="Clave")
cla.grid(column=2,row=10)
cla.configure(command=clave)

clean=ttk.Button(frm,text="Limpiar")
clean.grid(column=0,row=15,pady=10)
clean.configure(command=ClearText)

#MUESTRA DE RESULTADOS
Fresult_label = ttk.Label(frm)
Fresult_label.grid(row=4, column=1)
Sresult_label = ttk.Label(frm)
Sresult_label.grid(row=7, column=1)


root.mainloop()

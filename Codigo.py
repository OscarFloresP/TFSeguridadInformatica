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
    #Conversión del texto a lista para poder reemplazar letra por letra
    texto = list(texto.lower())

    for i in range(len(texto)):
        #Validación de espacios
        if texto[i] == ' ':
            texto[i] = ' '
        #Reemplazar el valor actual de la letra según la clave ingresada
        else:
            texto_output = alfabeto.index(texto[i]) + clave
            texto[i] = alfabeto[texto_output]
    #Conversión de lista a string
    output = ''.join(map(str, texto))
    return output


def descifrar(texto,clave):
    # Conversión del texto a lista para poder reemplazar letra por letra
    texto = list(texto.lower())

    for i in range(len(texto)):
        # Validación de espacios
        if texto[i] == ' ':
            texto[i] = ' '
        # Reemplazar el valor actual de la letra según la clave ingresada
        else:
            texto_output = alfabeto.index(texto[i]) - clave
            texto[i] = alfabeto[texto_output]
        #Conversión de lista a string
    output = ''.join(map(str, texto))
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

decry = StringVar()
decrybox = ttk.Entry(frm, textvariable=decry)
decrybox.grid(row=5, column=0)

def encriptado():
    try:
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

clean=ttk.Button(frm,text="Limpiar")
clean.grid(column=0,row=15,pady=10)
clean.configure(command=ClearText)

#MUESTRA DE RESULTADOS
Fresult_label = ttk.Label(frm)
Fresult_label.grid(row=4, column=1)
Sresult_label = ttk.Label(frm)
Sresult_label.grid(row=7, column=1)


root.mainloop()
import tkinter as tk
from tkinter import font

def calculoImc():
    try:
        peso = float(caja1.get())
        try:
            alt = float (caja2.get())
            imc = (peso/(alt**2))
            mensaje1.set("{:.2f}".format(imc))
            if imc<18.5:
                mensaje2.set("Bajo peso")
            elif imc>=18.5 and imc<=24.9:
                mensaje2.set ("Peso normal")
            elif imc>=25 and imc<=29.9:
                mensaje2.set("Sobrepeso")
            elif imc>=30 and imc<=34.9:
                mensaje2.set("Obesidad Tipo 1")
            elif imc>=35 and imc<=39.9:
                mensaje2.set("Obesidad Tipo 2")
            elif imc>=40:
                mensaje2.set("Obesidad Tipo 3")

        except ValueError as ve:
            mensaje3.set( "Debe ingresar un numero.\n Si es decimal debe utilizar el caracter punto")        
    except ValueError as ve:
        mensaje3.set( "Debe ingresar un numero.\n Si es decimal debe utilizar el caracter punto")

def limpiar():
    caja1.delete(0, tk.END) 
    caja2.delete(0, tk.END) 




ventana = tk.Tk()
ventana.title("Indice de Masa Corporal")
ventana.config(width=400, height=300)

etiqueta1 = tk.Label(text="Peso")
etiqueta1.place(x=50, y=50)

caja1 = tk.Entry()
caja1.place(x=100, y=50)

etiqueta2 = tk.Label(text="Altura")
etiqueta2.place(x=50, y=100)

caja2 = tk.Entry()
caja2.place(x=100, y=100)

boton1 = tk.Button(text="Calcular IMC",command=calculoImc )
boton1.place(x=100, y=130)

boton2 = tk.Button(text="Limpiar",command=limpiar )
boton2.place(x=200, y=130)

mensaje1 = tk.StringVar()
etiqueta3 = tk.Label(textvariable=mensaje1)
etiqueta3.place(x=100, y=170)
etiqueta3.config(fg="Blue", font="arial")

mensaje2 = tk.StringVar()
etiqueta4 = tk.Label(textvariable=mensaje2)
etiqueta4.place(x=100, y=200)

mensaje3 = tk.StringVar()
etiqueta4 = tk.Label(textvariable=mensaje3)
etiqueta4.place(x=50, y=220)



ventana.mainloop()
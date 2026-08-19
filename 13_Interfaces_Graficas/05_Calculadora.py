from tkinter import *

raiz = Tk()
raiz.title("Calculadora")

miFrame = Frame(raiz)
miFrame.pack()

operacion = ""
resultado = 0
reset_pantalla = False

#--------------- PANTALLA ----------------------------
numeroPantalla = StringVar()

pantalla = Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

#------------------Pulsaciones de teclado ---------------------
def numeroPulsado(num):
    global operacion
    global reset_pantalla

    if reset_pantalla:
        numeroPantalla.set(num)
        reset_pantalla = False
    else:
        numeroPantalla.set(numeroPantalla.get() + num)

#-----------------Funcion Suma ---------------------------------
def suma(num):
    global operacion
    global resultado
    global reset_pantalla

    resultado += int(num)
    operacion = "suma"
    reset_pantalla = True
    numeroPantalla.set(resultado)

#-----------------Funcion Resta ---------------------------------
def resta(num):
    global operacion
    global resultado
    global reset_pantalla

    if resultado == 0:
        resultado = int(num)
    else:
        resultado -= int(num)

    operacion = "resta"
    reset_pantalla = True
    numeroPantalla.set(resultado)

#-----------------Funcion Multiplicacion ------------------------
def multiplicacion(num):
    global operacion
    global resultado
    global reset_pantalla

    if resultado == 0:
        resultado = int(num)
    else:
        resultado *= int(num)

    operacion = "multiplicacion"
    reset_pantalla = True
    numeroPantalla.set(resultado)

#-----------------Funcion Division ------------------------------
def division(num):
    global operacion
    global resultado
    global reset_pantalla

    if resultado == 0:
        resultado = int(num)
    else:
        resultado /= int(num)

    operacion = "division"
    reset_pantalla = True
    numeroPantalla.set(resultado)

#-----------------Funcion Resultado ---------------------------------
def elResultado():
    global resultado
    global operacion
    global reset_pantalla

    if operacion == "suma":
        numeroPantalla.set(resultado + int(numeroPantalla.get()))
    elif operacion == "resta":
        numeroPantalla.set(resultado - int(numeroPantalla.get()))
    elif operacion == "multiplicacion":
        numeroPantalla.set(resultado * int(numeroPantalla.get()))
    elif operacion == "division":
        try:
            numeroPantalla.set(resultado / int(numeroPantalla.get()))
        except ZeroDivisionError:
            numeroPantalla.set("Error")

    resultado = 0
    operacion = ""
    reset_pantalla = True

# --------------- 1º FILA ------------------------------
boton7 = Button(miFrame, text="7", width=3, command=lambda: numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8 = Button(miFrame, text="8", width=3, command=lambda: numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9 = Button(miFrame, text="9", width=3, command=lambda: numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonDiv = Button(miFrame, text="/", width=3, command=lambda: division(numeroPantalla.get()))
botonDiv.grid(row=2, column=4)

# --------------- 2º FILA ------------------------------
boton4 = Button(miFrame, text="4", width=3, command=lambda: numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5 = Button(miFrame, text="5", width=3, command=lambda: numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6 = Button(miFrame, text="6", width=3, command=lambda: numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonMult = Button(miFrame, text="X", width=3, command=lambda: multiplicacion(numeroPantalla.get()))
botonMult.grid(row=3, column=4)

# --------------- 3º FILA ------------------------------
boton1 = Button(miFrame, text="1", width=3, command=lambda: numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2 = Button(miFrame, text="2", width=3, command=lambda: numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3 = Button(miFrame, text="3", width=3, command=lambda: numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonRes = Button(miFrame, text="-", width=3, command=lambda: resta(numeroPantalla.get()))
botonRes.grid(row=4, column=4)

# --------------- 4º FILA ------------------------------
boton0 = Button(miFrame, text="0", width=3, command=lambda: numeroPulsado("0"))
boton0.grid(row=5, column=1)
botonComa = Button(miFrame, text=",", width=3, command=lambda: numeroPulsado("."))
botonComa.grid(row=5, column=2)
botonIgual = Button(miFrame, text="=", width=3, command=lambda: elResultado())
botonIgual.grid(row=5, column=3)
botonMas = Button(miFrame, text="+", width=3, command=lambda: suma(numeroPantalla.get()))
botonMas.grid(row=5, column=4)

raiz.mainloop()
from tkinter import *

root = Tk()

varOpcion = IntVar()

def imprimit():
    #print(f"varOpcion: {varOpcion.get()}")
    if varOpcion.get() == 1:
        etiqueta.config(text="Masculino")
    else:
        etiqueta.config(text="Femenino")

Label(root, text="Género").pack()

Radiobutton(root, text="Masculino", variable=varOpcion, value=1).pack()
Radiobutton(root, text="Feminino", variable=varOpcion, value=2).pack()

etiqueta = Label(root)
root.mainloop()
from tkinter import *

root = Tk()
miFrame=Frame(root, width=500, height=500)
miFrame.pack()

#miImagen = PhotoImage(file="./imagen.png")

Label(
    miFrame,text="Ventana de pruebas",
    fg ="red",
    font=("Comic Sans MS",18)
).place(x=100,y=100)


root.mainloop()
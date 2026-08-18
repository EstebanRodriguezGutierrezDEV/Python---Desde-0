from tkinter import *

raiz = Tk()

raiz.title("Ventana de pruebas")
#raiz.resizable(width=True, height=True)#Esto sirve para no poder dimensionar la pantalla
raiz.iconbitmap("py.ico")#Cambia el icono de la aplicacion
#raiz.geometry("500x500")#redimensiona la ventana
raiz.config(bg="green")#Cambia el fondo de la pantalla

miFrame=Frame()
miFrame.pack()#Empaquetamos el Frame dentro de la raíz
miFrame.config(bg="blue")
miFrame.config(width="400",height="400")
miFrame.config(bd=35)#Esto es el borde
miFrame.config(relief="groove")#Esto es el tipo de borde
miFrame.config(cursor="pirate")

raiz.mainloop()#Esta instruccion debe estar siempre al final
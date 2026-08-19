from tkinter import *

root = Tk()

miFrame=Frame(root,width=1200,height=600)
miFrame.pack()

minombre = StringVar()

cuadroNombre = Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0,column=1,padx=10,pady=10)

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=1,column=1,padx=10,pady=10)

cuadroPass = Entry(miFrame)
cuadroPass.grid(row=2,column=1,padx=10,pady=10)
cuadroPass.config(show="*")

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3,column=1,padx=10,pady=10)

cuadroComentario = Text(miFrame, width=16,height=5,)
cuadroComentario.grid(row=4,column=1,padx=10,pady=10)

scrollVertical = Scrollbar(miFrame, command=cuadroComentario.yview)
scrollVertical.grid(row=4,column=2, sticky="nsew")
cuadroComentario.config(yscrollcommand=scrollVertical.set)

def codigoBoton():
    minombre.set("Esteban")

botonEnvio = Button(root,text="Enviar", command=codigoBoton)
botonEnvio.pack()

# LABELS

nombreLabel=Label(miFrame,text="Nombre:")
nombreLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)

apellidoLabel=Label(miFrame,text="Apellido:")
apellidoLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

cuadroPass=Label(miFrame,text="Contraseña:")
cuadroPass.grid(row=2,column=0,sticky="e",padx=10,pady=10)

direccionLabel=Label(miFrame,text="Dirección:")
direccionLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10)

comentarioLabel=Label(miFrame,text="Comentarios:")
comentarioLabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)



root.mainloop()
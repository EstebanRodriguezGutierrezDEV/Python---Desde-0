from tkinter import *
from tkinter import messagebox
import sqlite3
#-------------FUNCIONES--------------------
def conexionBBDD():
    miconexion=sqlite3.connect("Usuarios")
    miCursor=miconexion.cursor()

    try:
        miCursor.execute('''
            CREATE TABLE DATOSUSUARIOS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            APELLIDO VARCHAR(50),
            PASSWORD VARCHAR(50),
            DIRECCION VARCHAR(50),
            COMENTARIO VARCHAR(100)) 
        ''')
        messagebox.showinfo("BBDD", "BBDD creada con éxito")
    except:
        messagebox.showwarning("ATENCION", "La BBDD ya existe")

def salirAplicacion():
    valor=messagebox.askquestion("SALIR","¿Desas salir de la aplicación?")
    if valor == 'yes':
        root.destroy()


def limpiarCampos():
    miId.set("")
    miNombre.set("")
    miApellido.set("")
    miPass.set("")
    miDireccion.set("")
    cuadroComentarios.delete(1.0, END)


def crear():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()


    instruccion_sql = "INSERT INTO DATOSUSUARIOS VALUES(NULL, ?, ?, ?, ?, ?)"
    datos = (
        miNombre.get(),
        miApellido.get(),
        miPass.get(),
        miDireccion.get(),
        cuadroComentarios.get("1.0", "end-1c"),
    )

    miCursor.execute(instruccion_sql, datos)

    miConexion.commit()
    miConexion.close()
    messagebox.showinfo("BBDD", "Registro insertado con éxito")

def leer():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    instruccionSQL = "SELECT * FROM DATOSUSUARIOS WHERE ID = ?"
    dato = miId.get()

    miCursor.execute(instruccionSQL, (dato,))

    usuario = miCursor.fetchone()

    if usuario:
        miId.set(usuario[0])
        miNombre.set(usuario[1])
        miApellido.set(usuario[2])
        miDireccion.set(usuario[4])

        cuadroComentarios.delete(1.0, "end")
        cuadroComentarios.insert(1.0, usuario[5])
    else:
        print("Usuario no encontrado")

    miConexion.close()

def actualizar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()

    instruccion_sql = """
        UPDATE DATOSUSUARIOS 
        SET NOMBRE_USUARIO=?, APELLIDO=?, PASSWORD=?, DIRECCION=?, COMENTARIO=? 
        WHERE ID=?
    """


    datos = (
        miNombre.get(),
        miApellido.get(),
        miPass.get(),
        miDireccion.get(),
        cuadroComentarios.get("1.0", "end-1c"),
        miId.get()
    )

    miCursor.execute(instruccion_sql, datos)

    miConexion.commit()
    miConexion.close()

    messagebox.showinfo("BBDD", "Registro actualizado con éxito")


def borrar():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID=?", (miId.get(),))
    miConexion.commit()

    messagebox.showinfo("BBDD", "Los datos han sido borrados correctamente")

#--------------------------------------------
root = Tk()

barraMenu = Menu(root)
root.config(menu=barraMenu,width=300, height=300)

#--------Elementos barra menu---------------
bbddMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir",command=salirAplicacion)

borrarMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
borrarMenu.add_command(label="Borrar Campos",command=limpiarCampos)

crudMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)

crudMenu.add_command(label="Crear",command=crear)
crudMenu.add_command(label="Leer",command=leer)
crudMenu.add_command(label="Actualizar",command=actualizar)
crudMenu.add_command(label="Borrar",command=borrar)

ayudaMenu = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

#-------MAIN-(ZONA SUPERIOR)--------------
miFrame = Frame(root)
miFrame.pack()

miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

#-------ENTRY----------
cuadroId = Entry(miFrame,textvariable=miId)
cuadroId.grid(row=0,column=1,padx=10,pady=10)

cuadroNombre = Entry(miFrame,textvariable=miNombre)
cuadroNombre.grid(row=1,column=1,padx=10,pady=10)

cuadroApellido = Entry(miFrame,textvariable=miApellido)
cuadroApellido.grid(row=2,column=1,padx=10,pady=10)

cuadroContraseña = Entry(miFrame,textvariable=miPass)
cuadroContraseña.grid(row=3,column=1,padx=10,pady=10)
cuadroContraseña.config(show="*")

cuadroDireccion = Entry(miFrame,textvariable=miDireccion)
cuadroDireccion.grid(row=4,column=1,padx=10,pady=10)

cuadroComentarios = Text(miFrame, width=16,height=5)
cuadroComentarios.grid(row=5,column=1,padx=10,pady=10)

scrollVertical = Scrollbar(miFrame, command=cuadroComentarios.yview)
scrollVertical.grid(row=5,column=2, sticky="nsew")
cuadroComentarios.config(yscrollcommand=scrollVertical.set)

#-------LABELS--------------
idLabel=Label(miFrame,text="ID:")
idLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10)

nombreLabel=Label(miFrame,text="Nombre:")
nombreLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10)

apellidoLabel=Label(miFrame,text="Apellido:")
apellidoLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10)

PassLabel = Label(miFrame, text="Contraseña:")
PassLabel.grid(row=3,column=0,padx=10,pady=10)

direccionLabel=Label(miFrame,text="Dirección:")
direccionLabel.grid(row=4,column=0,sticky="e",padx=10,pady=10)

comentarioLabel=Label(miFrame,text="Comentario:")
comentarioLabel.grid(row=5,column=0,sticky="e",padx=10,pady=10)

#--------BOTONES---------------
miFrame2 = Frame(root)
miFrame2.pack()

botoncrear = Button(miFrame2, text="CREAR", command=crear)
botoncrear.grid(row=1, column=0, sticky="e", padx=10,pady=10)

botoncrear = Button(miFrame2, text="LEER", command=leer)
botoncrear.grid(row=1, column=1, sticky="e", padx=10,pady=10)

botoncrear = Button(miFrame2, text="ACTUALIZAR",command=actualizar)
botoncrear.grid(row=1, column=2, sticky="e", padx=10,pady=10)

botoncrear = Button(miFrame2, text="BORRAR",command=borrar)
botoncrear.grid(row=1, column=3, sticky="e", padx=10,pady=10)


root.mainloop()
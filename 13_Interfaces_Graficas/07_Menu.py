from tkinter import *
from tkinter import messagebox, filedialog  # Libreria para ventana emergente

root = Tk()
#-------------Funciones---------------------
def infoAicional():
    messagebox.showinfo("Acerca de...","Mi primera ventana emergente")

def avisoLicencia():
    messagebox.showwarning("Aviso","Mi segunda ventana emergente")

def salirAplicacion():
    #valor = messagebox.askquestion #yes o no
    valor = messagebox.askokcancel("Salir", "Deseas salir de la aplicación") #true o false
    if valor == True:
        root.destroy()

def cerrarDocumento():
    valor = messagebox.askretrycancel("Reintentar", "No es posible cerrar el documento")

def abreFichero():
    fichero = filedialog.askopenfilename(title="Abrir archivo", initialdir="C:", filetypes=(("Archivos", "*.*"),))
    print(fichero)


barraMenu = Menu(root)
root.config(menu=barraMenu,width=300,height=300)

#--------Elementos principales de Menu----------
archivoMenu = Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)

archivoEdicion = Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Editar", menu=archivoEdicion)

archivoHerramientas = Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)

archivoAyuda = Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

#--------SubMenus----------
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir", command=abreFichero)
archivoMenu.add_separator()
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar",command=cerrarDocumento)
archivoMenu.add_command(label="Salir",command=salirAplicacion)

archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")

archivoAyuda.add_command(label="Licencia",command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...", command=infoAicional)


root.mainloop()
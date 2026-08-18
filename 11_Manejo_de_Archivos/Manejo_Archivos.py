from io import open

archivo_texto = open ("texto.txt","w")#Si no existe lo cre sino lo abre

frase = "Estupendo día para aprender a crear y editar textos \n el día 18/08/26"
archivo_texto.write(frase)
archivo_texto.close()

archivo_texto = open ("texto.txt","r")
texto = archivo_texto.read()
archivo_texto.close()
print(texto)

print("-------------------------------------------")

archivo_texto = open ("texto.txt","r")
lineas_texto = archivo_texto.readlines() #Guarda la información dentro de una lista manipulable
archivo_texto.close()
print(lineas_texto)

print("-------------------------------------------")

archivo_texto = open ("texto.txt","a")#Es para agregar texto, pero no se muestra en consola solo en el archivo
frase2 = "\n siempre es bueno aprender cosas nuevas "
archivo_texto.write(frase2)

print("-------------------------------------------")

archivo_texto = open ("texto.txt","r")
print(archivo_texto.read())
archivo_texto.seek(0)#Imprime dos veces el mensaje por que cambia la posición del puntero
print(archivo_texto.read())
myDiccionary = {"Esteban":26, "Ines":23, "Elena":23}

myDiccionary["Juan"]=52 #Añadimos un elemento mas
print(myDiccionary)

del myDiccionary["Elena"] #Borra un elemento
print(myDiccionary)

print("-----------------------------------")

print("Añadimos clave por una tupla")

myTupla = ("España", "Francia", "Reino Unido" , "Alemania")
myDiccionary1 = {myTupla[0]:"Madrid", myTupla[1]:"París", myTupla[2]:"Londres", myTupla[3]:"Berlín"}
print(myDiccionary1)

print("-----------------------------------")

print("Como poder ver las claves y los valores del diccionario")

print(myDiccionary1.keys())#Vemos las claves
print(myDiccionary1.values())#Vemos los valores


print("-----------------------------------")

print("Como poder ver la longitud del diccionario")

print(len(myDiccionary1))

print("Listas")

myList = ["María","Pepe","Marta","Antonio"]

print(myList) #Imprime la lista completa
print(myList[0]) #Imprime un elemento concreto
print(myList[-2]) #Si el valor es negativo empieza a contar desde atras

print("----------------------------------------")

print("Porción de Lista")
print(myList[0:3]) #Excluye el ultimo elemnto ya que no se queda con el ultimo numero que se pone
print(myList[:2]) #Python entiende que es desde el indice 0
print(myList[2:])

print("----------------------------------------")

print("Añadir elementos")

myList.append("Sandra") #Agrega al final
myList.insert(1, "Manuel") #Agrega en el valor que le estamos dando
myList.extend(["Antonio","Ana","Lucía"]) #Agrega otra lista a la lista original (Al final)

print(myList)

print("----------------------------------------")

print("Saber el indice: Antonio")

print(myList.index("Antonio")) # Sirve para saber el indice de donde se encuentra el valor

print("Saber si un elemento se encuentra")

print("Pepe" in myList) #Imprime True o False si se encuentra o no 

print("----------------------------------------")

print("Otra lista con diferentes valores")

myList1 = ["Ines", 3, True, 78.5]

myList1.remove(3) #Silve para eliminar el valo 5 de la lista
myList1.pop() #Elimibna el ultimo elemento de la lista

print(myList1)

print("----------------------------------------")

print("Operadores en listas") #Concatena las listas

myList2 = myList1 + myList

print(myList2)
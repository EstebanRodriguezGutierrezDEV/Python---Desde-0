mytupla = ("Esteban", 12, 3, 2000)

myList = list(mytupla) #Combertimos a la tupla en una lista

print(mytupla[1])
print(myList) #Aqui es una lista 

print("-----------------------")

print("Combertimos una lista en una tupla")

myList1 = tuple(myList) 
print(myList1)

print("-----------------------")

print("Mira cuantas veces se encuentra un elemento")

print(mytupla.count(12))

print("-----------------------")

print("Vemos la longitud de una tupla")

print(len(mytupla)) #Me dice los elementos que hay 

print("-----------------------")

print("Damos una variable a cada valor de la tupla")

name, day, month, year = mytupla
print(name)
print(day)
print(month)
print(year)
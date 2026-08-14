list = ["primavera", "verano", "otoño", "invierno"]

for i in list:
    print(i,": Hola")

print("------------------------")

for i in "juan@pildorasinformaticas.es": #Se ejecuta tantas veces cuantos caracteres tenga este string
    print(i, end= " ")

print("------------------------")


miEmail = input("Intoduce el email: ").lower()
contador = 0

for i in miEmail: 
    if(i == "@" or i == "."):
        contador += 1

if contador == 2:
    print("El email es correcto")
else:
    print("El email no es correcto")


print("------------------------")

for i in range(0,51,5):# Esto quiere decir que va de 5 en 5 empezando en 0 y terminando en 50 
    print(f"Valor de la variable = {i}") #Concatena el texto con el valor de la variable


print("------------------------")

valido = False
email=input("Introduce tu email: ").lower()

for i in range(len(email)): #recorre cada caracter
    if email[i]=="@":
        valido = True

if valido:
    print("Email correcto")
else: 
    print("Email incorrecto")

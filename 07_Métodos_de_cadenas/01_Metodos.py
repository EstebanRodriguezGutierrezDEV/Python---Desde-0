nombreUsuario=input("Ingrese su nombre: ")
print(f"El nombre es: {nombreUsuario.upper()}")#Convierte el nombre a Mayus
print(f"El nombre es: {nombreUsuario.lower()}")#Convierte el nombre a Minus
print(f"El nombre es: {nombreUsuario.capitalize()}")#Convierte la primera letra en Mayus

print("-----------------------------------------------------")

edad=input("Introduce su edad: ")

while(edad.isdigit() == False):
    print("Por favor, introduzca un valor numérico.")
    edad=input("Introduce su edad: ")

if (int(edad)<18):
    print("No puede pasar")
else:
    print("Puede pasar")
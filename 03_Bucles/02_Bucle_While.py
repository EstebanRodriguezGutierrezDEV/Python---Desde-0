import math


i = 0

while i < 10:
    i += 1
    print("Ejecución" + str(i))

print("Programa finalizado")

print("--------------------------")

edad = int(input("Introduce tu edad porfavor: "))

while edad < 5 or edad > 100:
    print("Has ingresado la edad negativa. vuelve ha intentarlo")
    edad = int(input("Introduce tu edad porfavor: "))

print("Gracias por colaborar. Puedes pasar")
print(f"Edad del aspirante es: {str(edad)}")

print("------------------------------------------")

print("PROGAMA DE CALCULO DE RAÍZ CUADRADA")

num = int(input("Introduce un número, por favor: "))

intentos = 1

while num < 0:
    print("No se puede hayar la raíz de un número negativo")

    if intentos == 2:
        print("Has consumido demasiados intentos, intentalo de nuevo mas tarde")
        break #Sale del bucle while

    num = int(input("Introduce un número, por favor: "))
    if num <0:
        intentos += 1

if intentos < 2:
    solucion = math.sqrt(num) #Esto sirve para hayar la raiz cuadrada
    print(f"La raiz del número {str(num)} es {str(solucion)}")
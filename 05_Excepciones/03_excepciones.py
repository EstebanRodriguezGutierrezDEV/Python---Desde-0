import math

def evaluaEdad(edad):
    if edad <0:
        raise ValueError("No se permiten edades negativas") #Se puede usar TypeError y personalizar la salida del error

    if edad<20:
        return "Eres muy joven"
    elif edad <40:
        return "Eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad <100:
        return "Cuidate..."

print(evaluaEdad(18))

print("--------------------------------------------")

def calculaRaiz(num1):
    if num1<0:
        raise ValueError("El numero no puede ser negativo")
    else:
        return math.sqrt(num1)

op1=(int(input("Introduce un numero: ")))
try:
    print(calculaRaiz(op1))
except ValueError as ErrorDeNumNegativo: #Le puedo dar un nombre personalizado a la excepción
    print(ErrorDeNumNegativo)

print("Programa finalizado")

    

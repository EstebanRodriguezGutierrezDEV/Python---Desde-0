for letra in "Python":

    if letra == "h":
        continue #A cada vuelta de bucle lo comprueba y si encuentra una h pasa a la sigueinte

    print(f"Viendo la letra: {letra}")

print("----------------------------------------")

nombre = "Pildoras Informáticas"
contador = 0

for i in nombre:
    if i == " ":
        continue
    contador += 1

print(contador)

print("----------------------------------------")

class MiClase:
    pass #Para implementar mas tarde 

print("----------------------------------------")

email = input("Introduce tu email: ")

for i in email:
    if i == "@":
        arroba = True

        break;
else:
    arroba = False

print(arroba)

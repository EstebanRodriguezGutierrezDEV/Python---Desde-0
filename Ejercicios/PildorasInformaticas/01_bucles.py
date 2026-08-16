#Crea un programa que muestre los números impares del 1 al 100.
# Los números deberán
# aparecer una al lado del otro sin salto de línea.

listaPar =[]
listaImpar = []
for i in range(1, 101):
    if(i % 2 == 0):
        listaPar.append(i)
    else:
        listaImpar.append(i)

for num in listaImpar:
    print(num, end=" ")

print("________________________________________")
print("________________________________________")

#Crea un programa que pida por teclado introducir una contraseña. La contraseña no
#podrá tener menos de 8 caracteres ni espacios en blanco. Si la contraseña es correcta,
#el programa imprime “Contraseña OK”. En caso contrario imprime “Contraseña
#errónea”

password = input("Introduce una contraseña de 8 caracteres: ")
contador = 0
for i in password:
    contador += 1

if(contador < 8 or i == " " or contador < 0):
    print("Contraseña incorrecta")
else:
    print("Contraseña Correcta")
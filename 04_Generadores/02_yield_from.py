def devuelve_ciudades(*ciudades): # El asterisco indica al programa que va recibir un numero indeterminado de elementos y como tupla
    for elemento in ciudades:
        for sub_Elemento in elemento:
            yield sub_Elemento

ciudades_devueltas = devuelve_ciudades("Madrid","Barcelona","Sevilla","Bilbao")

#Con la funcion next va cogiendo de uno en uno los elementos y asi los va devolviendo
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

print("__________________________________")

#Codigo anterior simplificado

def devuelve_ciudades1(*ciudades1): # El asterisco indica al programa que va recibir un numero indeterminado de elementos y como tupla
    for elemento1 in ciudades1:
        yield from elemento1

ciudades_devueltas1 = devuelve_ciudades1("Madrid","Barcelona","Sevilla","Bilbao")

#Con la funcion next va cogiendo de uno en uno los elementos y asi los va devolviendo
print(next(ciudades_devueltas1))
print(next(ciudades_devueltas1))
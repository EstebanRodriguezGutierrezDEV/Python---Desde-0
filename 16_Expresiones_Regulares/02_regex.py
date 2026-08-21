import re
lista_nombres =['Ana Gómez',
                'María Martín',
                'Sandra Lopez',
                'Santiago Martín']

lista_url=['http://www.pildorasinformaticas.es',
            'ftp://www.pildorasinformaticas.es',
            'https://www.pildorasinformaticas.com',
            'https://www.pildorasinformaticas.com']

lista_personas =['Hombre',
                'Mujer',
                'Niño',
                 'Niña']

for nombre in lista_nombres:
    if re.findall('^Sandra', nombre): #Empieza por
        print(nombre)

for nombre in lista_nombres:
    if re.findall('Martín$', nombre):# termina por
        print(nombre)

for nombre in lista_url:
    if re.findall('es$', nombre):# termina por
        print(nombre)

for nombre in lista_url:
    if re.findall('^ftp', nombre):# Empieza
        print(nombre)

for letra in lista_personas:
    if re.findall('Niñ[oa]', letra):# Empieza
        print(letra)
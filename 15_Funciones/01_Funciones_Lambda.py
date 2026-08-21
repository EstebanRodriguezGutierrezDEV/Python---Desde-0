area_triangulo = lambda base, altura: (base * altura)/2
print(area_triangulo(5, 15))

al_cubo = lambda numero:pow(numero,3)
#al_cubo = lambda numero:numero**3
print(al_cubo(5))

destacar_valor = lambda comision: "¡{}!$".format(comision)

comision_Ana=1585
print(destacar_valor(comision_Ana))
edad = -7

# Utilizando la concatenación con concatenadores de comparación
print("Concatenacion de operadores de comperación")
if 0 < edad < 100 :
    print("Edad es correcta")
else:
    print("Edad incorrecta")


print("------------------------------")

salario_presidente = int(input("Introduce el salario presidente: "))
print("Salario presidente: ", str(salario_presidente))

salario_director = int(input("Introduce el salario del director: "))
print("Salario diretor: ", str(salario_director))

salario_jefe_area = int(input("Introduce el salario del jefe de area: "))
print("Salario jefe de area: ", str(salario_jefe_area))

salario_administrativo = int(input("Introduce el salario del administrativo: "))
print("Salario administrativo: ", str(salario_administrativo))

if salario_presidente > salario_director > salario_jefe_area > salario_administrativo:
    print("Todo funciona correctamente")
else:
    print("Algo huele mal")

print("------------------------------")

print("PROGRMA BECAS 2026")
alumno = input("Introduce el nombre del alumno: ")
distancia = int(input("Introduce la distancia que vives del centro: "))
num_hermanos = int(input("Dime cuantos hermanos compeneis la familia: "))
salarioa_fam = int(input("Dime cualñ es la renta familiar: "))

if distancia > 40 and num_hermanos > 2 or salarioa_fam <=20000:
    print("La beca al alumno: ", alumno, " ha sido concedida")
else:
    print("No se le ha concedido la beca")

print("------------------------------")

print("ASIGNATURAS OPTATIVAS AÑO 2026")
print("Asiganturas Optativcas: Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")

opcion = input("Escrbe la asignatura escogida: ")
asignatura = opcion.lower()

if asignatura in ("Informatica grafica","Pruebas de software", "Usabiolidad y accesibilidad"):
    print("La asignatura escogida por el aulmno ha sido: ", asignatura)
else:
    print("No ha elegido una asignatura definida")
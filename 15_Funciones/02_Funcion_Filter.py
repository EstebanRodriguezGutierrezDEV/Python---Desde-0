class Empleado:
    def __init__(self,nombre,cargo, salario):
        self.nombre=nombre
        self.cargp=cargo
        self.salario=salario

    def __str__(self):
        return "{} que trabaja como {} tiene salario de {}$".format(self.nombre,self.cargp,self.salario)

listaEmpleados=[
    Empleado("Juan", "Director", 77000),
    Empleado("Ana", "Presidenta", 87000),
    Empleado("Pepe", "Administrativo", 25000),
]

salarios_altos=filter(lambda e: e.salario>50000,listaEmpleados)

for empleado in salarios_altos:
    print(empleado)
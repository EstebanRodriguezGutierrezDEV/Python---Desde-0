class Empleado:
    def __init__(self,nombre,cargo, salario):
        self.nombre=nombre
        self.cargp=cargo
        self.salario=salario

    def __str__(self):
        return "{} que trabaja como {} tiene salario de {}$".format(self.nombre,self.cargp,self.salario)

listaEmpleados=[
    Empleado("Juan", "Director", 6700),
    Empleado("Ana", "Presidenta", 7500),
    Empleado("Pepe", "Administrativo", 2100),
    Empleado("Mario","Botones",1800)
]

def calculo_comision(empleado):
    if empleado.salario <= 3000:
        empleado.salario = empleado.salario * 1.05

    return empleado

listaEmpleadosComision=map(calculo_comision,listaEmpleados)

for empleado in listaEmpleadosComision:
    print(empleado)
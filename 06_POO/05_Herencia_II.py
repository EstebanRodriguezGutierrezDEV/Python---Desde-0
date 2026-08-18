class Persona():
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion(self):
        print(f"Nombre: {self.nombre}\nEdad: {self.edad}\nLugar de residencia: {self.lugar_residencia}")

class Empleado(Persona):
    def __init__(self, salario, antigüedad,nombre_empleado, edad_empleado, residencia_empleado):
        #Al incluir esta instrucción esta heredando de la clase padre los atributos
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antigüedad = antigüedad

    def descripcion(self):
        super().descripcion() #Nos ahorramos repetir la linea de la clase padre
        print(f"Salario: {self.salario}\nAntiguedad: {self.antigüedad}")


Antonio=Persona("Antonio", 55, "España")
print(isinstance(Antonio, Persona))
print(isinstance(Antonio, Empleado))#Una Persona no tiene por que ser un empleado

Manuel=Empleado(1600, 20, "Manuel", 32, "Colombia")
print(isinstance(Manuel, Persona))
print(isinstance(Manuel, Empleado))

Antonio.descripcion()
Manuel.descripcion()
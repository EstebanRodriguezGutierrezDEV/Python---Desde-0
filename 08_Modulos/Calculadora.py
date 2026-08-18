class Calculadora():
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def pedir_numeros(self):
        self.a = int(input("Introduce el primer número: "))
        self.b = int(input("Introduce el segundo número: "))

    def sumar(self):
        self.pedir_numeros()
        resultado = self.a + self.b
        return f"El resultado de la suma de {self.a} + {self.b} = {resultado}"

    def restar(self):
        self.pedir_numeros()
        resultado = self.a - self.b
        return f"El resultado de la resta de {self.a} - {self.b} = {resultado}"

    def multiplicar(self):
        self.pedir_numeros()
        resultado = self.a * self.b
        return f"El resultado de la multiplicación de {self.a} x {self.b} = {resultado}"



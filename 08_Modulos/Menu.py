from Calculadora import Calculadora

class Menu(Calculadora):
    def ejecutar(self):
        op = 0
        while op != 4:
            print("\nElige una opción del menú (1-4)")
            print("-------------------------------")
            print("1-Sumar")
            print("2-Restar")
            print("3-Multiplicar")
            print("4-Salir")
            print("-------------------------------")
            op = int(input("Elige una opción: "))

            if op == 1:
                print(self.sumar())
            elif op == 2:
                print(self.restar())
            elif op == 3:
                print(self.multiplicar())
            elif op == 4:
                print("Gracias por usar la calculadora")
            else:
                print("Opción inválida")

app = Menu()
app.ejecutar()
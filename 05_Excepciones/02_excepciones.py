def divide():

    while True:
        try:

            op1 = float(input("Introduce el primer numero: "))
            op2 = float(input("Introduce el segundo numero: "))

            print(f"La division es {str(op1/op2)}")

            break

        except ValueError:
            print("El valor introducido es erroneo")

        except ZeroDivisionError:
            print("No se puede dividr entre 0")
            
        finally:
            print("Calculo finalizado")

divide()
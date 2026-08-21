def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args, **kwargs):
        print("Vamos a realizar un calculo: ")
        funcion_parametro(*args,**kwargs)

        #Acciones adicionales que decoran
        print("Hemos terminado el calculo")

    return funcion_interior

#Cuando se haga la llamada a la funcion suma tiene mas acciones adicionales
@funcion_decoradora
def suma(num1,num2):
    print(num1 + num2)

@funcion_decoradora
def resta(num1, num2):
    print(num1 - num2)

@funcion_decoradora
def potencia(base,exponente):
    print(pow(base, exponente))

suma(7,5)
resta(12,10)
potencia(base=5,exponente=3)
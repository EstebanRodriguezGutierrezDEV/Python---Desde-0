class Coche():

    def __init__(self): #Constructor
        # PROPIEDADES
        self.largoChasis = 250
        self.color = "rojo"
        self.caballos = 300
        self.ruedas = 4
        self.enmarcha = False



    #COMPORTAMIENTOS
    def arrancar(self,arrancamos):
        self.enmarcha=arrancamos
        if(self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

    def estado(self):
        print("El coche teine ", self.ruedas, "ruedas. Un largo de ", self.largoChasis, " y  ", self.caballos, " caballos")

miCoche = Coche() #Instanciamos una clase

print(f"El largo del coche es: {miCoche.largoChasis}")
print(f"El coche tiene: {miCoche.ruedas} ruedas")

print(miCoche.arrancar(True))
print(miCoche.estado())

print("-------------Acontinuacion creamos el segundo objeto----------")

miCoche2 = Coche()

print(f"El largo del coche es: {miCoche2.largoChasis}")
print(f"El coche tiene: {miCoche2.ruedas} ruedas")

print(miCoche2.arrancar(False))

miCoche2.ruedas = 5 #Modificamos el valor de la propiedad

print(miCoche2.estado())
class Coche():

    #PROPIEDADES
    largoChasis=250
    color="rojo"
    caballos=300
    ruedas=4
    enmarcha=False

    #COMPORTAMIENTOS
    def arrancar(self,arrancamos):
        self.enmarcha=arrancamos
        if(self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

    def estado(self):
        if self.enmarcha:
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

miCoche = Coche() #Instanciamos una clase

print(f"El largo del coche es: {miCoche.largoChasis}")
print(f"El coche tiene: {miCoche.ruedas} ruedas")

miCoche.arrancar()
print(miCoche.estado())

print("-------------Acontinuacion creamos el segundo objeto----------")

miCoche2 = Coche()

print(f"El largo del coche es: {miCoche2.largoChasis}")
print(f"El coche tiene: {miCoche2.ruedas} ruedas")

miCoche2.arrancar()
print(miCoche2.estado())
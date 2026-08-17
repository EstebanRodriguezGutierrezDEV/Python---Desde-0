class Coche():

    def __init__(self): #Constructor
        # PROPIEDADES
        self.__largoChasis = 250
        self.__color = "rojo"
        self.__caballos = 300
        self.__ruedas = 4
        self.__enmarcha = False



    #COMPORTAMIENTOS
    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"

        elif(self.__enmarcha and chequeo == False):
            return "Algo ha ido mal, no podemas arrancar"

        else:
            return "El coche esta parado"

    def estado(self):
        print("El coche teine ", self.__ruedas, "ruedas. Un largo de ", self.__largoChasis, " y  ", self.__caballos, " caballos")

    def __chequeo_interno(self):
        print(f"Realizando chequeo interno...")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return  True
        else:
            return False



miCoche = Coche() #Instanciamos una clase
print(miCoche.arrancar(True))
print(miCoche.estado())


print("-------------Acontinuacion creamos el segundo objeto----------")

miCoche2 = Coche()
print(miCoche2.arrancar(False))
print(miCoche2.estado())

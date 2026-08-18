class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=Coche()
miVehiculo.desplazamiento()

miVehiculo2=Moto()
desplazamientoVehiculo(miVehiculo2)#Aqui ocurre el polimorfismo

miVehiculo3=Camion()
miVehiculo3.desplazamiento()
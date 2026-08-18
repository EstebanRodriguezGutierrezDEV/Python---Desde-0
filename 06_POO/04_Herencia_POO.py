class Vehiculos():
    def __init__(self, marca, modelo): #Constructor
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frena(self):
        self.frena = True

    def estado(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nAcelera: {self.acelera}\nFrena: {self.frena}\nEnmarcha: {self.enmarcha}")

class Furgoneta(Vehiculos):
    def cargada(self, cargar):
        self.cargado = cargar
        if(self.cargado):
            return "La furgonerta esta cargada"
        else:
            return "La furgonerta no esta cargada"

class Moto(Vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito= "Voy haciendo el caballito"

    def estado(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nAcelera: {self.acelera}\nFrena: {self.frena}\nEnmarcha: {self.enmarcha}\n{self.hcaballito}")

class VElectricos(Vehiculos):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True



miMoto = Moto("Honda", "CBR")
miFurgoneta = Furgoneta("Renault", "Kangoo")

miMoto.caballito()
miMoto.estado()

print("-------------------------------------")

miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.cargada(True))

print("-------------------------------------")

class BicicletaElectrica(VElectricos): #Se le da mas importancia a los metodos del primer atributo
    pass

miBici = BicicletaElectrica("Orbea","HC1030")

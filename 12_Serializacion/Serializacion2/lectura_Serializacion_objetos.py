import pickle

class Vehiculo():
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelerar = False
        self.frenar = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelerar = True

    def frenar(self):
        self.frenar = True

    def estado(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nEnmarcha: {self.enmarcha} \nAcelerar: {self.acelerar} \nFrenar: {self.frenar}")

ficheroApertura = open("losCoches", "rb")
misCoches = pickle.load(ficheroApertura)

for c in misCoches:
    print(c.estado())
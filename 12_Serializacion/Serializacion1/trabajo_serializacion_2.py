import pickle

fichero = open("lsita_nombres", "rb")

lista = pickle.load(fichero)

print(lista)
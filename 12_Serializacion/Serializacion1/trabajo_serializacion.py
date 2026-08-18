import pickle

lista_nombres = ["Pedro","Ana","María","Isabel"]

fichero_binario = open("lsita_nombres", "wb")#Escribe en binario

pickle.dump(lista_nombres,fichero_binario)

fichero_binario.close()
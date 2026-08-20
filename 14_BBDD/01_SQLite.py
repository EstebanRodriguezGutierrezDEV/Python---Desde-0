import sqlite3

miConexion = sqlite3.connect("PrimeraBBDD")

miCursor = miConexion.cursor()

#Esto solo debe ejecutarse una vez
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#Insertar un registro en la BBDD
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN',15,'DEPORTES')")

#Insertar un lote de registros
#variosProductos = [
#    ("Camiseta",10,"Deportes"),
#    ("Jarrón",90,"Cerámica"),
#    ("Camión",30,"Juguetes")
#]
#miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", variosProductos)

#Mustra la información de la BD en consola
#miCursor.execute("SELECT * FROM PRODUCTOS")
#variosProductos = miCursor.fetchall()
#for producto in variosProductos:
#    print(producto)




miConexion.commit()

miConexion.close()
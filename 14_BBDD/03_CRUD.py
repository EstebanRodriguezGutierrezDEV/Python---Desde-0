import sqlite3

miConexion = sqlite3.connect("GestionProductos")
miCursor = miConexion.cursor()

miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION = 'Cerámica'")
miCursor.execute("UPDATE PRODUCTOS SET PRECIO = 25 WHERE NOMBRE_ARTICULO = 'Pelota'" )
miCursor.execute("DELETE FROM PRODUCTOS WHERE ID = 4")

miConexion.commit()
import sqlite3

miConexion = sqlite3.connect("GestionProductos")
miCursor = miConexion.cursor()

miCursor.execute('''
    CREATE TABLE PRODUCTOS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        CODIGO_ARTICULO VARCHAR(4) UNIQUE,
        NOMBRE_ARTICULO VARCHAR(50),
        PRECIO INTEGER,
        SECCION VARCHAR(20))
''')

productos = [
    ("AR01","Pelota",20,"Juguete"),
    ("AR02","Pantalón",15,"Ropa"),
    ("AR03","Destornillador",25,"Ferretería"),
    ("AR04","Jarrón",45,"Cerámica"),
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?,?)", productos)

miConexion.commit()

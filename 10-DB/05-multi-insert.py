#CONEXION A UNA BASE DE DATOS
import sqlite3  


#WITH PERMITE REALIZAR EL CLOSE Y EL COMMIT SIN SOLICITARLO
with sqlite3.connect("10-DB/app.db") as con:
    cursor = con.cursor()


    ##INSERTAR MULTIPLES TUPLAS A LA DB
    usuraios = [
        (2, "Santiago Feliz"),
        (3, "Santiago Triste")
    ]
    cursor.executemany(
        "insert into usuraios values(?, ?)",
        usuraios,

    )
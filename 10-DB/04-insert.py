#CONEXION A UNA BASE DE DATOS
import sqlite3  


#WITH PERMITE REALIZAR EL CLOSE Y EL COMMIT SIN SOLICITARLO
with sqlite3.connect("10-DB/app.db") as con:
    cursor = con.cursor()
    #insertar valores
    cursor.execute(
        "insert into usuraios values(?, ?)",
        (1,"Hola Mundo"),
    )
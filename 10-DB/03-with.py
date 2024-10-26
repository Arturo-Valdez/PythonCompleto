#CONEXION A UNA BASE DE DATOS
import sqlite3  


#WITH PERMITE REALIZAR EL CLOSE Y EL COMMIT SIN SOLICITARLO
with sqlite3.connect("10-DB/app.db") as con:
    cursor = con.cursor()

    #EJECUTAR UNA CONSULTA
    cursor.execute(
        """
        CREATE TABLE if not exists usuraios
        (id INTEGER primary key, nombre VARCHAR(50));
        """
    )


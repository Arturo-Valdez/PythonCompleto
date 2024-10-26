#CONEXION A UNA BASE DE DATOS
import sqlite3  

con = sqlite3.connect("10-DB/app.db")
cursor = con.cursor()

#EJECUTAR UNA CONSULTA
cursor.execute(
    """
    CREATE TABLE if not exists usuraios
    (id INTEGER primary key, nombre VARCHAR(50));
    """
)
#COMPROMETER CONSULTA SINO NO SE EJECUTARA
con.commit()
con.close()


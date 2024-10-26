#CONEXION A UNA BASE DE DATOS
import sqlite3  


#WITH PERMITE REALIZAR EL CLOSE Y EL COMMIT SIN SOLICITARLO
with sqlite3.connect("10-DB/app.db") as con:
    cursor = con.cursor()
    #CONSULTA SQL
    cursor.execute("SELECT * from usuraios")
    #MUESTRA SOLO EL PRIMER REGISTRO QUE SE TIENE
    print(cursor.fetchone())#(1, 'Hola Mundo')
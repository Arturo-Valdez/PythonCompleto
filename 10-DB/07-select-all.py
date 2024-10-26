#CONEXION A UNA BASE DE DATOS
import sqlite3  


#WITH PERMITE REALIZAR EL CLOSE Y EL COMMIT SIN SOLICITARLO
with sqlite3.connect("10-DB/app.db") as con:
    cursor = con.cursor()
    #CONSULTA SQL
    cursor.execute("SELECT * from usuraios")
    #MUESTRA TODOS LOS REGISTRO QUE SE TIENEN
    print(cursor.fetchall())#[(1, 'Hola Mundo'), (2, 'Santiago Feliz'), (3, 'Santiago Triste')]
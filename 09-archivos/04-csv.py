import csv
import os
# escribir

# with open("09-archivos/archivo.csv", "w", newline = '') as archivo:
#     writer = csv.writer(archivo)
#     writer.writerow(["wit_id", "user_id", "text"])
#     writer.writerow([1000, 1, "Este es un twit"])
#     writer.writerow([1001, 2, "otro twit"])  



#leer
# with open("09-archivos/archivo.csv") as archivo:
#     reader = csv.reader(archivo)
#     print(list(reader))
#     archivo.seek(0)
#     for linea in reader:
#         print(linea)


# actualizar CSV

with open("09-archivos/archivo.csv") as r, open("09-archivos/archivo_temp.csv", "w", newline='') as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for linea in reader:
        if linea[0] == "1000":
            writer.writerow([1000, 1, "Texto modificado 2"])
        else:
            writer.writerow(linea)
    
    # Reemplazar archivos
os.remove("09-archivos/archivo.csv")
os.rename("09-archivos/archivo_temp.csv", "09-archivos/archivo.csv")


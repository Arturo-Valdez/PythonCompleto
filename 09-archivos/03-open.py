from io import open

#Escritura
# texto = "Hola mundo"

# archivo = open("09-archivos/hola-mundo.txt", "w")
# archivo.write(texto)
# archivo.close()

# /////////////////////////////////////////////////////////////////////////////////
# # lectura
# archivo = open("09-archivos/hola-mundo.txt", "r")
# texto = archivo.read()
# archivo.close()
# print(texto)

# ///////////////////////////////////////////////////////////////////////
# # Leer como lista
# archivo = open("09-archivos/hola-mundo.txt", "r")
# texto = archivo.readlines()
# archivo.close()
# print(texto)


# //////////////////////////////////////////////////////////////////////////////////////
# #with y seek
# with open("09-archivos/hola-mundo.txt", "r") as archivo:
#     print(archivo.readlines())
#     archivo.seek(0)
#     for linea in archivo:
#         print(linea)


# ////////////////////////////////////////////////////////////////////////////////////////////

# agregar
# archivo = open("09-archivos/hola-mundo.txt", "a+")
# archivo.write("Chao mundo :(")
# archivo.close()

# //////////////////////////////////////////////////////////////////////////////////////////////

#lectura y escritura
with open("09-archivos/hola-mundo.txt", "r+") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = "Santiago Feliz mas mas"
    print(texto)
    archivo.writelines(texto)
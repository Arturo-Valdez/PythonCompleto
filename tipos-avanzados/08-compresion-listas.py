usuarios = [
    ["Chanchito", 4], 
    ["Prdito", 1], 
    ["Paquillo", 5]
    ]

#Obtener solo el nombre con una nueva lista
# nombres=  []

# for usuario in usuarios:
#     nombres.append(usuario[0]) 
# print(nombres)#['Chanchito', 'Prdito', 'Paquillo']


#SEGUNDA FORMA transformamos y creamos nueva lista
#variable   expresion   ciclo   variablede interacion   en      lista usuarios
# nombres =   [usuario[0] for     usuario                 in      usuarios]
# print(nombres)#['Chanchito', 'Prdito', 'Paquillo']


#FILTRAR ELEMENTOS
# Extrae los valores mayores en la posicion de indice los mayores a 2
# nombre = [usuario for usuario in usuarios if usuario[1] > 2]
# print(nombre)#[['Chanchito', 4], ['Paquillo', 5]]


# FILTRAR Y EXTRAER
# toma el valor usuario de posicion 0 crea un ciclo donde interas a usuario en usuarios y si el indice
# es mayor a 2
nombre = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombre)#['Chanchito', 'Paquillo']
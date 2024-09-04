diccionarioPunto = {"x": 25,
                    "y": 50
                    }

#LAS COMILLAS SIMPLES SON LLAVES
print(diccionarioPunto)#{'x': 25, 'y': 50}
print(diccionarioPunto["x"])#25
print(diccionarioPunto["y"])#50

# Agregar elementos en diccionario
diccionarioPunto["z"]= 45

print(diccionarioPunto)#{'x': 25, 'y': 50, 'z': '45'}

print(diccionarioPunto["z"])#45

#Muestra diccionario y valor de la llave "x"
print(diccionarioPunto, diccionarioPunto["x"])#{'x': 25, 'y': 50, 'z': '45'} 25

#Elimina llaves y sus valores de diccionario
del diccionarioPunto["x"]
del diccionarioPunto["y"]

print(diccionarioPunto)#{'z': '45'}


diccionarioPunto["x"] = 77

#imprime la llavez
# x
# y
# z
for valor in diccionarioPunto:
    print(valor)


#SE OBTIENE LAS LLAVES Y LOS VALORES DEL DCCIONARIO
# ('z', 45)
# ('x', 77)
for valor in diccionarioPunto:
    print(valor, diccionarioPunto[valor])


#MEJOR 
#Imprime el la llave y su valor en forma de tuplas
# ('x', 25)
# ('y', 50)
# ('z', '45'
for valor in diccionarioPunto.items():
    print(valor)




if "lala" in diccionarioPunto:
    print(f"Si se encuentra 'lala' con valor = {diccionarioPunto['lala']}")
else:
    print(diccionarioPunto.get("lala"))#None

    #crea la llave lala con un valor mas no lo agrega al diccionario
    print(diccionarioPunto.get("lala", 101))#101

    print(diccionarioPunto)#{'x': 25, 'y': 50, 'z': '45'}




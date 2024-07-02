#LAS TUPLAS NO LAS PUEDES MODIFICAR - AGREGAR - NI QUITAR ELEMENTOS
#PUEDES TENER SUS VALORES PERO NO PUEDES MODIFICAR

numeros = (1,2,3) + (4,5,6)
print(numeros)#(1, 2, 3, 4, 5, 6)

#VOLVER UNA LISTA EN TUPLA
punto = tuple([1,2])
print(punto)#(1, 2)

#CREAR UNA NUEVA TUPLA CON LOS PRIMEROS VALORES DE 0 A 2
menosNumeros = numeros[:2]
print(menosNumeros)#(1, 2)

#DESEMPAQUETAR TUPLAS
primero, segundo, *otros = numeros
print(primero, segundo, otros) #1 2 [3, 4, 5, 6]


#INTERAR LA TUPLA
# 1
# 2
# 3
# 4
# 5
# 6
for n in numeros:
    print(n)


#CREAR UNA LISTA CON ELEMENTOS DE LA TUPLA
#SI SE PUEDE MODIFICAR
listNumeros = list(numeros)
listNumeros[2] = "Hola Mundo"
print(listNumeros)#[1, 2, 'Hola Mundo', 4, 5, 6]
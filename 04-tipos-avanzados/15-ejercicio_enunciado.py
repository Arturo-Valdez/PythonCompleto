from pprint import pprint #PERMITE SALTO DE LINEA LIBRERIA



#1. ELIMINAR LOS ESPACIOS EN BLANCO DE UN STRING 
#   Y DEVOLVER UNA LISTA CON LOS CARACTERES RESTANTES

#2.CONTAR EN UN DICCIONARIO CUANTO SE REPITEN LOS CARACTERES EN UN STRING

#3.ORDENAR LAS LLAVES DE UN DICCIONARIO POR EL VALOR QUE TIENEN
#   Y DEVOLVER UNA LISTA QUE CONTIENE TUPLAS 
#[("a",3),("b",2),("c",4),("d",4)]

#4.DE UN LISTADO DE TUPLAS DEVOLVER LAS TUPLAS QUE TENGAN
#EL MAYOR VALOR

#5.CREAR MENSAJE QUE DIGA
# LOS CARACTERES QUE MAS SE REPITEN CON 4 REPETICIONES SON
# - C
#   D

# 6.JUNTAR LAS SOLUCION DE LOS EJERCICIOS ANTERIORES
# PARA ENCONTRAR LOS CARACTERES QUE MAS SE REPITEN DE UN STRING

# ////////////////////////////////////////////////////////////////////////////
#1. ELIMINAR LOS ESPACIOS EN BLANCO DE UN STRING 
#   Y DEVOLVER UNA LISTA CON LOS CARACTERES RESTANTES

string = "Hola mundo este es mi string"

def quitar_espacios(texto):
    #Retorna una comprension de listas
    return [char for char in texto if char != " "]

sin_espacios = quitar_espacios(string)
#['H', 'o', 'l', 'a', 'm', 'u', 'n', 'd', 'o', 'e', 's', 't', 'e', 'e', 's', 'm', 'i', 's', 't', 'r', 'i', 'n', 'g']
print(sin_espacios)

#//////////////////////////////////////////////////////////////////////////////////

#2.CONTAR EN UN DICCIONARIO CUANTO SE REPITEN LOS CARACTERES EN UN STRING

def cuenta_caracteres(lista):
    #se crea el diccionario
    chars_dict = {}
    # intera lista
    for char in lista:
        #si la llave es igual a alguna llave del diccionario
        #a su valor sumale 1
        if char in chars_dict:
              chars_dict[char] += 1
        #sino solo dale 1
        else:
            chars_dict[char] = 1
        #retorna el diccionaerio
    return chars_dict

contado = cuenta_caracteres(sin_espacios)
# {'H': 1,
#  'a': 1,
#  'd': 1,
#  'e': 3,
#  'g': 1,
#  'i': 2,
#  'l': 1,
#  'm': 2,
#  'n': 2,
#  'o': 2,
#  'r': 1,
#  's': 3,
#  't': 2,
#  'u': 1}
pprint(contado, width=1)



#///////////////////////////////////////////////////////////////////////////////////////////


#3.ORDENAR LAS LLAVES DE UN DICCIONARIO POR EL VALOR QUE TIENEN
#   Y DEVOLVER UNA LISTA QUE CONTIENE TUPLAS 
#[("a",3),("b",2),("c",4),("d",4)]


def ordena(dict):
    return sorted(
    dict.items(),
    key=lambda key:key[1], reverse=True
    )

ordenados = ordena(contado)
#[('e', 3), ('s', 3), ('o', 2), ('m', 2), ('n', 2), ('t', 2), ('i', 2), ('H', 1), ('l', 1), ('a', 1), ('u', 1), ('d', 1), ('r', 1), ('g', 1)]
print(ordenados)


#///////////////////////////////////////////////////////////////////////////////////////////
#4.DE UN LISTADO DE TUPLAS DEVOLVER LAS TUPLAS QUE TENGAN
#EL MAYOR VALOR


def mayores_tuplas(lista):
    maximo = lista[0][1]
    respuesta = {}
    for orden in lista:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta


mayores = mayores_tuplas(ordenados)
#{'e': 3, 's': 3}
print(mayores)

#/////////////////////////////////////////////////////////////////////////////////
#5.CREAR MENSAJE QUE DIGA
# LOS CARACTERES QUE MAS SE REPITEN CON 4 REPETICIONES SON
# - C
#   D

def crea_mensaje(diccionario):
    mensaje = "Los qe mas se repiten son \n"
    for key, valor in diccionario.items():
        mensaje += f"-{key} con {valor} repeticiones \n"
    return mensaje

mensaje = crea_mensaje(mayores)
# Los qe mas se repiten son
# -e con 3 repeticiones
# -s con 3 repeticiones
print(mensaje)
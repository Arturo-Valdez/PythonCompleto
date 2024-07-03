lista = [1,2,3,4]
print(1,2,3,4)
#se desempaqueta la lista
print(*lista)

# TODO LAS LISTAS USAN UN SOLO * YA QUE USAN UN SOLO VALOR,LOS DICCIONARIOS USAN ** YA QUE TIENEN LLAVE Y VALOR
#DESEMPAQUETADO
primero, segundo, *lista = lista
print(primero, segundo)#1 2

#COMBINACION DE LISTAS
lista1 = [1,2,3,4]
Lista2 = [4,5]
conbinadas = ["Hola", *lista1, "mundo", *Lista2, "Santiago"]
print(conbinadas)#['Hola', 1, 2, 3, 4, 'mundo', [4, 5], 'Santiago']


#COMBINACION DE DICCIONARIOS
#Se elimina de derecha a izquierda 
punto1 = {"x":19, "y":12}
punto2 = {"y":30}

combinadasDiccionarios = {"z":"Hola", **punto1, "r":"rol", **punto2, "t":"Todos"}
print(combinadasDiccionarios)#{'z': 'Hola', 'x': 19, 'y': 30, 'r': 'rol', 't': 'Todos'}
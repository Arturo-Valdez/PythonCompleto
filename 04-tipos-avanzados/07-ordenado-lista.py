numeros = [74, 55, 41112, 5, 21, 1, 1, 6, 3, 1]

# Se obtiene valor de la cantidad de elementos que hay en numeros
n = len(numeros)

# Se realiza un bucle anidado para ordenamiento de menor a mayor
for i in range(n):
    for j in range(n):
        #Si el valor de i es menor que j 
        if numeros[i] < numeros[j]:
            #Se coloca el valor de i en aux
            aux = numeros[i]
            #se coloca el valor de j en i
            numeros[i] = numeros[j]
            # se coloca el valor de aux en j
            numeros[j] = aux

# [1, 1, 1, 3, 5, 6, 21, 55, 74, 41112]
print(numeros)



# Se realiza un bucle anidado para ordenamiento de mayor a menor
for i in range(n):
    for j in range(n):
        #Si el valor de i es menor que j 
        if numeros[i] > numeros[j]:
            #Se coloca el valor de i en aux
            aux = numeros[i]
            #se coloca el valor de j en i
            numeros[i] = numeros[j]
            # se coloca el valor de aux en j
            numeros[j] = aux

# [41112, 74, 55, 21, 6, 5, 3, 1, 1, 1]
print(numeros)


#///////////////////////////////////////////////////////////////////////////////////////////


#Ordenamiento con una funcion de Sort menor a mayor
#[1, 1, 1, 3, 5, 6, 21, 55, 74, 41112]
numeros.sort()
print(numeros)

#Ordenamiento con una funcion de Sort con reverse = Tue ordena de mayor a menor
# [41112, 74, 55, 21, 6, 5, 3, 1, 1, 1]
numeros.sort(reverse=True)
print(numeros)





numeros = [74, 55, 41112, 5, 21, 1, 1, 6, 3, 1]

#Ordena y rea una nueva lista sin afectar a la original ordenado de menor a mayor
numeros2 = sorted(numeros)
print(numeros2)#[1, 1, 1, 3, 5, 6, 21, 55, 74, 41112]
print(numeros)#[74, 55, 41112, 5, 21, 1, 1, 6, 3, 1].



#Ordena y rea una nueva lista sin afectar a la original ordenado de mayor a menor
numeros2 = sorted(numeros, reverse=True)
print(numeros2)#[41112, 74, 55, 21, 6, 5, 3, 1, 1, 1]
print(numeros)#[74, 55, 41112, 5, 21, 1, 1, 6, 3, 1]




#///////////////////////////////////////////////////////////////////////////////////////
#ODENAMIENTO POR ID
usuarios = [
    [4, "Chanchito"], 
    [1,"Prdito"], 
    [5, "Paquillo"]
    ]

#Se realiza ordenamiento ya que se pasa el valor id al comienzo, pero si fuera primero
#el String fallaria el ordenamiento
usuarios.sort()
print(usuarios)#[[1, 'Prdito'], [4, 'Chanchito'], [5, 'Paquillo']]


#ERROR DE ORDENAMIENTO
usuarios = [
    ["Chanchito", 4], 
    ["Prdito", 1], 
    ["Paquillo", 5]
    ]

#Se realiza ordenamiento ya que se pasa el valor id al comienzo, pero si fuera primero
#el String fallaria el ordenamiento
usuarios.sort()
print(usuarios)#[['Chanchito', 4], ['Paquillo', 5], ['Prdito', 1]]





#ERROR DE ORDENAMIENTO / AJUSTE DE ORDENAMIENTO CON KEY
usuarios = [
    ["Chanchito", 4], 
    ["Prdito", 1], 
    ["Paquillo", 5]
    ]

#Se realiza ordenamiento ya que se pasa el valor id al comienzo, pero si fuera primero
#el String fallaria el ordenamiento


def ordena(elemento):
    return elemento[1]
#Ordena con la llave tomando con la posicion 1
usuarios.sort(key=ordena)
print(usuarios)#[['Prdito', 1], ['Chanchito', 4], ['Paquillo', 5]]

numeros = [1,2,3]

# #FEO
# primero = numeros[0]
# segundo= numeros[1]
# tercero = numeros[2]

# print(primero, segundo, tercero) # 1 2 3


#FORMA CORTA
primero, segundo, tercero = numeros
print(primero, segundo, tercero) # 1 2 3

#Toma el primer valor y asignalo a la variable primero
#
primero, *otros = numeros 
print(primero, otros) #1 [2, 3]


#Se asigna nuevos valores a la lista
numeros = list(range(1,11)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros)

#Tomar el primer valor y el segundo
primero, segundo, *otros = numeros #1 2 [3, 4, 5, 6, 7, 8, 9, 10]
print(primero, segundo, otros) 


#Tomar el primer valor y el ultimo
primero, *otros, ultimo = numeros #1 10 [2, 3, 4, 5, 6, 7, 8, 9]
print(primero, ultimo, otros) 

#Tomar el segundo valor y el penultimo
primero,segundo, *otros, penultimo ,ultimo = numeros #2 9 [3, 4, 5, 6, 7, 8]
print(segundo, penultimo, otros) 
# LIFO
#LI --> lAST IN
#FO -- > FIRST OUT

#EJEMPLO HISTORIAR DE NAVEGACION

# Se crea una lista de funcion pila
pila = []

# Se agrega elemento
pila.append(1)
# Se agrega elemento
pila.append(2)
# Se agrega elemento
pila.append(3)
# Se agrega elemento
pila.append(4)

print(pila)#[1, 2, 3, 4]

ultimoElemento = pila.pop()

print(ultimoElemento)#4

# Se elimino ultimo elemento
print(pila)#[1, 2, 3]

#Se eliminan ultimos elementos
pila.pop()
pila.pop()
pila.pop()

if not pila:
    print("Pila vacia")
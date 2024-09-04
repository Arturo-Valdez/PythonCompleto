# Ejercicio 1: En el lenguaje que te sientas más cómodo, utilizando un algoritmo recursivo, genera una función que reciba como parámetro un número entero como parámetro y calcule su factorial. (evite el uso de librerías predefinidas para el cálculo)

# Ejemplos:

# Parámetro 5 Retorno 120

# Parámetro 9 Retorno 362880

# Factorial es un valor que se multiplica por su valor anterior
# 5! = 5 * 4 * 3 * 2 * 1

def factorial(valor):
    if valor == 0 or valor == 1:
        return 1
    elif valor < 0:
        return "Solo colocar valores positivos"
    else:
        return valor * factorial(valor - 1)

print(factorial(5))#120

print(factorial(-5))#"Solo colocar valores positivos"

print(factorial(0))#1

print(factorial(1))#1
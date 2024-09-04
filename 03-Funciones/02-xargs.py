#LA IDENTACION ES IMPORTANTE PARA QUE UNA FUNCION SE EJECUTE CORRECTAMENTE
# Permite agregar todos los argumentos y  parametros que se quieran
def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

suma(2,4)
suma(2,4,454,41,22)
suma(2,4,454,41,22,4,454,41,22)
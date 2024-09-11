def division(n=0):
    if n==0:
        #raise ZeroDivisionError(...): Esta instrucción se utiliza para lanzar una excepción.
        raise ZeroDivisionError(f"No se puede dividir entre 0, {n}")
    return 5/n

try:
    division()

except ZeroDivisionError as e:
    print(e)

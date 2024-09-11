class MiError(Exception):
    "ESTA CLASE ES PARA REPRECENTAR MI ERROR"

    def __init__(self, mensaje, codigo):
        self.mensaje = mensaje
        self.codigo = codigo

    def __str__(self):
        return f"{self.mensaje} - codigo: {self.codigo}"

def division(n=0):
    if n==0:
        #raise ZeroDivisionError(...): Esta instrucción se utiliza para lanzar una excepción.
        raise MiError("No se puede dividir entre 0", 805)
    return 5/n

try:
    division()

except MiError as e:
    print(e)

# No usar variables globales

saludo = "Hola Hola"
def saludar():
    global saludo
    print(saludo)
    saludo = "Hola Mundo"
    print(saludo)


def saludarChanchito():
    saludo ="Hola Chanchito"
    print(saludo)

saludar()
saludarChanchito()
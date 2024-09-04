

class Usuario():
    def guardar(self):
        print("guardado en BBDD")

class Sesion():
    def guardar(self):
        print("guardado en archivo")

def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()

usaurio = Usuario()
sesion = Sesion()

#POLIMORFISMO
guardar([sesion, usaurio])
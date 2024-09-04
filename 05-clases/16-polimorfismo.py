from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass


class Usuario(Model):
    def guardar(self):
        print("guardado en BBDD")

class Sesion(Model):
    def guardar(self):
        print("guardado en archivo")

def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()

usaurio = Usuario()
sesion = Sesion()

#POLIMORFISMO
guardar([sesion, usaurio])
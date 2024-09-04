from abc import ABC, abstractmethod

#Se crea metodo abstracto para no permitir su uso
class Model(ABC):
    @property
    @abstractmethod
    def tabla(self):
        pass
    @abstractmethod
    def guardar(self):
        pass

    @classmethod
    def buscar_por_id(self, _id):
        print(f"Buscando por id {_id} en la tabla {self.tabla}")

class Usuario(Model):
    tabla = "Usuario"

    def guardar(self):
        print("Guardando usuario")

#INSTANCIA
usuario = Usuario()
usuario.guardar()#Guardando usuario
Usuario.buscar_por_id(123)#Buscando por id 123 en la tabla Usuario
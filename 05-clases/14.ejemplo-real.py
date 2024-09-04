# """
# Leer
# Crear
# Actualizar
# Eliminar


# Datos:
# Nombre
# Apellido
# Impuesto
# """

class Model():
    #atributo
    tabla = False
    #Constructor
    def __init__(self):
        if not self.tabla:
            print("Error, tienes que definir una tabla")

    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")

    @classmethod
    def buscar_por_id(self, _id):
        print(f"Buscando por id {_id} en la tabla {self.tabla}")

class Usuario(Model):
    tabla = "Usuario"

#INSTANCIA
usuario = Usuario()


usuario.guardar()#Guardando Usuario en BBDD

#Se realiza busqueda desde la clase
Usuario.buscar_por_id(123)#Buscando por id 123 en la tabla Usuario

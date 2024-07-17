# PROPIEDAD Y ATRIBUTO SON EXACTAMENTE LO MISMO

class Perro:
    patas = 4

    #CONSTRUCTOR, Siempre el primer parametro es self
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    #Trasfrma el metodo habla en un metodo propio de Perro
    @classmethod
    # "METODO", CLS es llamar a perro
    def habla(cls):
        print("Guau!")

    #FACTORY METHOD  / CREA INSTANCIAS DE LA CLASE
    @classmethod
    def factory(cls):
        return cls("Brunito", 4)

Perro.habla()
perro1 = Perro("Bruno", 2)
perro2 = Perro("Cupo de nieve", 3)
perro3 = Perro.factory()
print(perro3.edad, perro3.nombre) #4 Brunito
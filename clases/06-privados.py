# PROPIEDAD Y ATRIBUTO SON EXACTAMENTE LO MISMO

class Perro:
    patas = 4

    #CONSTRUCTOR, Siempre el primer parametro es self
    def __init__(self, nombre, edad):
        #Propiedades privadas NO SE PUEDE ACCEDER NI MODIFICAR DESDE AFUERA
        self.__nombre = nombre
        self.edad = edad

    #CCEDER AL VALOR DE NOMBRE
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    # "METODO", CLS es llamar a perro
    def habla(self):
        print(f"{self.__nombre} tiene edad de {self.edad} años y dice Guau!")

    #FACTORY METHOD  / CREA INSTANCIAS DE LA CLASE
    @classmethod
    def factory(cls):
        return cls("Brunito", 4)
    
perro1 = Perro.factory()
perro1.habla()
# ERROR PARA MOSTRAR VALOR PRIVADO
#  print(perro1.__nombre) // 'Perro' object has no attribute '__nombre
#print(perro1.__nombre)


#METODO PARA ACCEDER AL VALOR DE NOMBRE PRIVADO
print(perro1.get_nombre())

#MODIFICA EL VALOR DE NOMBRE
perro1.set_nombre("Pedrito")
perro1.habla()

#MUESTRA TODAS LAS PROPIEDADES DE LA CLASE Perro
# {'_Perro__nombre': 'Pedrito', 'edad': 4}
print(perro1.__dict__)

#FORMA PARA ACCEDER AL VALOR DE UNA VALIRABLE PRIBADA
#SIN EMBARGO NO ES ETICO REALIZARLO YA QUE ES PRIVADO
print(perro1._Perro__nombre)




# PROPIEDAD Y ATRIBUTO SON EXACTAMENTE LO MISMO

class Perro:
    patas = 4

    #CONSTRUCTOR
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # "METODO", Siempre el primer parametro es self
    def habla(self):
        print(f"{self.nombre} tiene edad de {self.edad} años y dice Guau!")

# CAMBIA EL VALOR DE PANTAS EN TODA LA CLASE
Perro.patas = 3
mi_perro = Perro("Bruno", 0.4)
mi_perro2 = Perro("Cupo de nieve", 1)
# CAMBIA EL VALOR DE PATAS UNICAMENTE EN MI INSTANCIA mi_perro
mi_perro.patas = 6
print(Perro.patas)#3
print(mi_perro.patas)#6
print(mi_perro2.patas)#3

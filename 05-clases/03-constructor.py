class Perro:
    #CONSTRUCTOR
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # "METODO", Siempre el primer parametro es self
    def habla(self):
        print(f"{self.nombre} tiene edad de {self.edad} años y dice Guau!")

mi_perro = Perro("Bruno", 0.4)
mi_perro2 = Perro("Cupo de nieve", 1)
print(mi_perro.nombre)#Bruno
print(mi_perro2.nombre)#Cupo de nieve

#Bruno tiene edad de 0.4 años y dice Guau!
mi_perro.habla()
#Cupo de nieve tiene edad de 1 años y dice Guau!
mi_perro2.habla()
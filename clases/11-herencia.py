# herencia en Python, donde se crean clases y se demuestran las relaciones de herencia entre ellas.
class Animal:
    def comer(self):
        print("Comiendo")

animal = Animal()
animal.comer()
print("Clase Animal \n")

#/////////////////////////////////////////////////////////////////////
class Perro(Animal):
    def pasear(self):
        print("Paseando")

perro = Perro()    
perro.comer()
perro.pasear()
print("Clase Perro, heredando Clase Animal \n")

#//////////////////////////////////////////////////////////////////////////
class Santiago(Perro):
    def programar(self):
        print("Programando")

santiago = Santiago()
santiago.comer()
santiago.pasear()
santiago.programar()
print("Clase Santiago hereda Clase Perro y heredando Clase Animal \n")
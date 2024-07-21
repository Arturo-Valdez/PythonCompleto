#https://rszalski.github.io/magicmethods/


class Perro:
    #This is a constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    # El método __del__ en Python se utiliza para definir cómo debe comportarse un objeto justo antes de que sea destruido y liberado de la memoria.
    def __del__(self):
        print(f"Chao Perro 😔 {self.nombre}")


    # Este método __str__ parece estar diseñado para devolver una representación de cadena (string) del objeto de la clase Perro. El método __str__ en Python se utiliza para definir cómo se debe representar un objeto como cadena cuando se imprime o se convierte explícitamente a cadena.
    def __str__(self):
        return f"Clase Perro: {self.nombre}"

    #This is a Method
    def habla(self):
        print(f"{self.nombre} dice: Guau!")

perro = Perro("Bruno", 0.5)
# print(perro)#Clase Perro: Bruno


del perro#Chao Perro 😔 Bruno
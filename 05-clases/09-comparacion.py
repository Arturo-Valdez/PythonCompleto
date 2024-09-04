class Coordenadas:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud

    #El método __eq__ en Python es un método especial que se utiliza para definir la igualdad entre dos objetos de una clase. Cuando defines __eq__, estás especificando cómo se debe comparar una instancia de la clase con otra para determinar si son consideradas iguales.
    def __eq__(self, otro):
        return self.latitud == otro.latitud and self.longitud == otro.longitud

    #El método __ne__ en Python es otro método especial que se utiliza para definir la desigualdad entre dos objetos de una clase. Este método se invoca cuando utilizas el operador != para comparar dos instancias de la clase y determinar si no son iguales.
    def __ne__(self, otro):
        return self.latitud != otro.latitud or self.longitud != otro.longitud
    
    #El método __lt__ en Python es un método especial que se utiliza para definir el operador de comparación "menor que" (<) entre dos objetos de una clase. Este método se llama cuando utilizas los operadores de comparación para determinar si una instancia es menor que otra según algún criterio específico que definas en la implementación del método.
    def __lt__(self, otro):
        return self.latitud + self.longitud < otro.latitud + otro.longitud

    
    #Parece que estás definiendo el método __le__ en una clase de Python. El método __le__ se utiliza para definir el comportamiento del operador menor o igual (<=).
    def __le__(self, otro):
        return self.latitud + self.longitud <= otro.latitud + otro.longitud



coords = Coordenadas(45,17)
coords2 = Coordenadas(45,27)

#USO DE __eq__ 
#Falce
print(coords == coords2)

#USO DE __ne__
# True
print(coords != coords2)

#USO DE __lt__
#True
print(coords < coords2)

#USO DE __le__
#False
print(coords >= coords2)
class Perro:
    #CONSTRUCTOR
    def __init__(self, nombre):
        self.nombre = nombre
    

    #Property es un getter que devuelve un valor
    @property
    def nombre(self):
        print("Este es un getter")
        return self.__nombre
    
    #Se encarga se cambiar el valor de nombre
    @nombre.setter
    def nombre(self, nombre):
        print("Este es un Setter")
        #evalúa si después de eliminar los espacios en blanco, la cadena nombre resultante no es vacía.
        # Si la cadena no es vacía (es decir, tiene al menos un carácter visible), el cuerpo del if se ejecutará.
        if nombre.strip():
            self.__nombre = nombre
        return 
    
    

perro = Perro("Bruno colita de algodon")
#Este es un Setter
# Este es un getter
# Bruno
print(perro.nombre)



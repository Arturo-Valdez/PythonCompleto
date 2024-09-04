#TODA CLASE DEBE LLEVAR LA PRIMERA LETRA MAYUSCULA EN CADA
#PALABRA POR ("PASCAL CASE // UpperCamelCase")
class Perro:
    # "METODO", Siempre el primer parametro es self
    def habla(self):
        print("Guau!")

mi_perro = Perro()
print(type(mi_perro))#<class '__main__.Perro'>

mi_perro.habla()#Guau!


#PREGNTAR SI  el objeto es una instancia de dicha clase o de una subclase es TRUE
print(isinstance(mi_perro, Perro))#"True"
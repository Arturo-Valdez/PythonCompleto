#Se agregan 2 parametros nombre y apellido
def hola(nombre, apellido):
    print("hola")
    print(f"Bienvenido {nombre} {apellido}")

#Se pasan 2 argumentos
hola("Santiago", "Valdez")
hola("Chanchito","Feliz")


#Se agregan 2 parametros nombre y apellido, pero apellido si no se encuentra 
#argumento se pondra Feliz sin marca de error
def hola2(nombre, apellido = "Feliz"):
    print("hola")
    print(f"Bienvenido {nombre} {apellido}")

hola2("Chanchito")

#Ajustar datos junto a su parametro con su argumento
hola(apellido="Valdez", nombre="Santiago")
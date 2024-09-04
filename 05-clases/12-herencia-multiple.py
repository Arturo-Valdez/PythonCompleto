# herencia múltiple y cómo los métodos se resuelven en una jerarquía de herencia compleja. 

class Caminador:
    # Clase que define el método camina.
    def camina(self):
        print("Caminando")

class Volador:
    # Clase que define el método volar.
    def volar(self):
        print("Volando")


class Nadador:
    #Clase que define el método nadar.
    def nadar(self):
        print("Nadando")



#////////////////////////////////////////////////////////
#Perro: Hereda de Caminador y Nadador, lo que significa que puede usar los métodos camina y nadar, y define su propio método habla.
class Perro(Caminador, Nadador):
    def habla(self):
        print("Ladrando")
        
#PezVolador: Hereda de Volador y Nadador, lo que significa que puede usar los métodos volar y nadar, y define su propio método habla.
class PezVolador(Volador, Nadador):
    def habla(self):
        print("BloBlu")
        
# Pato: Hereda de Caminador, Nadador, y Volador, lo que significa que puede usar los métodos camina, nadar, y volar, y define su propio método habla.
class Pato(Caminador, Nadador, Volador):
    def habla(self):
        print("Cuack")

print("Pato")
pato = Pato()
pato.volar()
pato.habla()
pato.camina()
pato.nadar()
print("\n")

print("Perro")
perro = Perro()
perro.habla()
perro.camina()
perro.camina()
print("\n")

print("Pez Volador")
pezVolador = PezVolador()
pezVolador.habla()
pezVolador.volar()
pezVolador.nadar()
print("\n")

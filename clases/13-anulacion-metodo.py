
#CLASE PADRE
class Ave:
    def __init__(self):
        self.volador = "Volador"
        
    def vuela(self):
        print("Vuela ave")

#SUBCLASE
class Pato(Ave):
    def __init__(self):
        self.nada = "Nadador"
        #PALABRA RECERBADA DE super, NOS DEVUELVE TODOS LOS METODOS Y
        #PROPIEDADES DEL PADRE
        super().__init__()

    def vuela(self):
        #PALABRA RECERBADA DE super, NOS DEVUELVE TODOS LOS METODOS Y
        #PROPIEDADES DEL PADRE
        super().vuela()
        print("Vuela pato")


pato = Pato()
# Vuela ave
# Vuela pato
pato.vuela()

#Volador Nadador
print(pato.volador, pato.nada)
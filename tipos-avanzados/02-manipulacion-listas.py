mascotas = ["Bruno", "Pelusa", "Pulga", "Princesa"]
print(mascotas[0])

mascotas[0] = "Bicho" #Cambio de nombre de Bruno a Bicho
print(mascotas[0]) #Bicho

print(mascotas) #['Bicho', 'Pelusa', 'Pulga', 'Princesa']
                    #   0           1       2
print(mascotas[:3]) #['Bicho', 'Pelusa', 'Pulga']
print(mascotas[2:]) # ['Pulga', 'Princesa'] Cuenta desde la posicion 2 hasta el ultimo elemento
print(mascotas[2:3]) #['Pulga'] -Toma el elemento entre las posiciones 2 a 3
print(mascotas[-1]) #Princesa  - Como no hay valor -1 en la lista toma la ultima posicion que seria la 3
print(mascotas[::2]) #['Bicho', 'Pulga'] SALTA LA POSICION 1 QUE ES Pelusa ya que toma los valores pares
print(mascotas[1:2:2]) #['Pelusa'] - Inicia en peluza, llega a posicion 2 y toma valores pares


numeros = list(range(21))
print(numeros) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(numeros[::2]) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20] - Inicia desde la primera posicion, lee toda la lista y toma valores pares
print(numeros[1::2]) #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19] - Inicia en la posicion 1, lee toda la lista y toma valores pares
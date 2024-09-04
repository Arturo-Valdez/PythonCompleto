mascotas = ["Peluza", "Pulga", "Felipe", "Pachuco","Chachito Feliz", "Pachuco"]


#Agregar elemento en posicion espesifico y su valor
# ['Peluza', 'Malvin', 'Pulga', 'Felipe', 'Pachuco', 'Chachito Feliz', 'Pachuco']
mascotas.insert(1, "Malvin")
print(mascotas)

#Agrega en la ultima posicion de la lista nuevo elemento
# ['Peluza', 'Malvin', 'Pulga', 'Felipe', 'Pachuco', 'Chachito Feliz', 'Pachuco', 'Chanchito triste']
mascotas.append("Chanchito triste")
print(mascotas)

#ELIMINA EL ELEMENTO Nota: el primer elemento, si existiesen mas, no haria nada con ellos
# ['Peluza', 'Malvin', 'Felipe', 'Pachuco', 'Chachito Feliz', 'Pachuco', 'Chanchito triste']
mascotas.remove("Pulga")
print(mascotas)


#Elimina el ultimo valor de la lista
# ['Peluza', 'Malvin', 'Felipe', 'Pachuco', 'Chachito Feliz', 'Pachuco']
mascotas.pop()
print(mascotas)

#Elimina el valor de la lista con su indice en especifico
# ['Peluza', 'Malvin', 'Pachuco', 'Felipe', 'Pachuco', 'Chachito Feliz', 'Pachuco', 'Pachuco', 'Pachuco']
mascotas.pop(2)
print(mascotas)

# Elimina el valor con el indice 2da opcion
# ['Malvin', 'Pachuco', 'Chachito Feliz', 'Pachuco']
del mascotas[0]
print(mascotas)

#Limpia toda la lista dejandola vacia
# []
mascotas.clear()
print(mascotas)
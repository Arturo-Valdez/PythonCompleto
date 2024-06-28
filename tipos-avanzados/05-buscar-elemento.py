mascotas = ["Peluza", "Pulga", "Felipe", "Pachuco","Chachito Feliz", "Pachuco"]

#Muestra la posicion donde se encuentra el elemento
# print(mascotas.index("Felipes")) #2



#Muestra la posicion donde se encuentra el elemento
if "Pachuco" in mascotas:
     print(mascotas.index("Pachuco"))
else:
     print("Elemento no encontrado")

#Muestra cuantos elementos con ese nombre se encuentran en la lista
print(mascotas.count("Pachuco"))
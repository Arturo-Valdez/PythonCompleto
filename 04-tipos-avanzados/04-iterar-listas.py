mascotas = ["Peluza", "Pulga", "Felipe", "Chachito Feliz"]

#Muestra los valores que contiene la lista
# Peluza
# Pulga
# Felipe
# Chachito Feliz
for mascota in mascotas:
    print(mascota)


# TUPLA
# (0, 'Peluza')
# (1, 'Pulga')
# (2, 'Felipe')
# (3, 'Chachito Feliz')
for mascota in enumerate(mascotas):
    print(mascota)

#Si se coloca el lugar 0, es de los indices
# 0
# 1
# 2
# 3
for mascota in enumerate(mascotas):
    print(mascota[0])

#Si se coloca el lugar 1, es de los valores
# Peluza
# Pulga
# Felipe
# Chachito Feliz
for mascota in enumerate(mascotas):
    print(mascota[1])



#Acceder a los INDICES de una lista agragando indice y mascota en tupla
# 0 Peluza
# 1 Pulga
# 2 Felipe
# 3 Chachito Feliz
for indice, mascota in enumerate(mascotas):
    print(indice, mascota)
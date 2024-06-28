mascotas = ["Pachuco","Peluza", "Pulga", "Felipe", "Pachuco","Chachito Feliz", "Pachuco","Pachuco"]


print(mascotas.count("Pachuco"))

#Intera hasta que mascotas sea solo 1
# ['Peluza', 'Pulga', 'Felipe', 'Chachito Feliz', 'Pachuco']
while mascotas.count("Pachuco") > 1:
    mascotas.remove("Pachuco")
print(mascotas)
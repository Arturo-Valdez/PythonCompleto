usuarios = [
    ["Chanchito", 4], 
    ["Prdito", 1], 
    ["Paquillo", 5]
    ]


nombre = list(map(lambda usuario: usuario[0], usuarios))
print(nombre)#['Chanchito', 'Prdito', 'Paquillo']


menosUsuarios = list(filter(lambda usuario : usuario[1]>2, usuarios))
print(menosUsuarios)#[['Chanchito', 4], ['Paquillo', 5]]



menosUsuarios = list(filter(lambda usuario : usuario[1]>2 and usuario[1]<5, usuarios))
print(menosUsuarios)#[['Chanchito', 4]]
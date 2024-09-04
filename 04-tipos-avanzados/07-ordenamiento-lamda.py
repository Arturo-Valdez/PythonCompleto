usuarios = [
    ["Chanchito", 4], 
    ["Prdito", 1], 
    ["Paquillo", 5]
    ]


#La funcion lambda es una funcion anonima, pero no es muy recomendable
usuarios.sort(key=lambda elemento:elemento[1])
print(usuarios)#[['Prdito', 1], ['Chanchito', 4], ['Paquillo', 5]]
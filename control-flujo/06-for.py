
#FOR
# for numero in range(5):
#     print(numero, numero * "Hola mundo ")


#FOR ELSE
buscar = 10
for numero in range(5): #iterable de 0 - 4
    print(numero)
    if numero == buscar:
        print("Encontrado ", buscar)
        break
else:
    print("No encontre lo buscado :c")




for char in "Saniago Valdez":
    print(char)
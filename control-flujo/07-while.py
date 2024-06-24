# numero = 1

# while numero < 100:
#     print(numero)
#     numero*=2


#Comando de salida
# comando = ""

# #funcion lower() hace toda la informacion en minusculas
# while comando.lower() != "salir":
#     comando = input("$ ")
#     print(comando)

while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() != "salir":
        break
#EJERCICIO PARECIDO AL USO DE BASE DE DATOS

#LISTA DE DICCIONARIOS
usuarios = [
    {"id": 1, "nombre":"Karen"},
    {"id": 2, "nombre":"Carlos"},
    {"id": 3, "nombre":"Joel"},
    {"id": 4, "nombre":"Hugo"},
    {"id": 5, "nombre":"Jorge"},
    {"id": 6, "nombre":"Roberto"},
    {"id": 7, "nombre":"Hernesto"},
    {"id": 8, "nombre":"Heriberto"},
]

#OBTENER TODOS LOS USUARIOS
# Karen
# Joel
# Hugo
# Jorge
# Roberto
# Hernesto
# Heriberto
for usuario in usuarios:
    print(usuario["nombre"])
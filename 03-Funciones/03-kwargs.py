
# KeyWorksArguments empaquetar todos los parametros de agumentos.
def get_product(**datos):
    print(datos["id"],datos["name"],datos["desc"])

get_product(id="24", name= "iPhone", desc="Esto es un equipo celular potente")
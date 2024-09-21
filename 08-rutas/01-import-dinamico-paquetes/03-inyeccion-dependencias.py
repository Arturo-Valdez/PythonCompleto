from pathlib import Path
# import db
# import graphql
# import api

path = Path()
paths = [p for p in path.iterdir( ) if p.is_dir()]

dependencias = {
    "db": "base de datos", #cambiar a db
    "api": "esta es la api",#cambiar a api
    "graphql": "esto es graphql"#cambiar a graphql
}

def load(p):
    paquete = __import__(str(p).replace("/", "."))

    try:
        paquete.init(**dependencias)
    except:
        print("El paquete no tiene funcion")

list(map(load, paths))

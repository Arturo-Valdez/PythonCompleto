#JSON  
#JS --> JAVASCRIPT
#O --> OBJECT
#N --> NOTETION
import json
from pathlib import Path

#escribir json
# productos = [
#     {"id" : 1, "name" : "Surfboard"},
#     {"id" : 2, "name" : "Bicicleta"},
#     {"id" : 3, "name" : "Skate"},
# ]

# data = json.dumps(productos)

# Path("09-archivos/productos.json").write_text(data)


#leer Json
data = Path("09-archivos/productos.json").read_text(encoding="utf-8")
productos = json.loads(data)
print(productos)


#modificar json
productos[0]["name"] = "Santiago Feliz"
Path("09-archivos/productos.json").write_text(json.dumps( productos))


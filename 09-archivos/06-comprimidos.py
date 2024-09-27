from pathlib import Path
from zipfile import ZipFile

# ESCRIBIR ARCHIVOS COMPRIMIDOS
# with ZipFile("09-archivos/comprimidos.zip", "w")  as zip:
#     for path in Path().rglob("*.*"):
#         print(path)
#         if str(path) != "09-archivos/comprimidos.zip" and str(path) != " ../format.py":
#             zip.write(path)


# #leer archivos comprimidos
with ZipFile("09-archivos/comprimidos.zip")  as zip:
    # print(zip.namelist())
    info = zip.getinfo("09-archivos/06-comprimidos.py")
    print(
        info.file_size,
        info.compress_size,
        )
    zip.extractall("archivos/descomprimidos")
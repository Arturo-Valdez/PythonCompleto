from pathlib import Path
from time import ctime
archivo = Path("09-archivos/archivo-prueba.txt")

# #verificar existencia
# archivo.exists()
# #renombrar archivo
# archivo.rename()
# #Eliminar el archivo
# archivo.unlink()

#Muestra las caracteristicas del arcivo
# os.stat_result(st_mode=33206, st_ino=12103423998579279, st_dev=17916534534188367254, st_nlink=1, st_uid=0, st_gid=0, st_size=5252, st_atime=1727060718, st_mtime=1727060718, st_ctime=1727060643)
# print(archivo.stat())


# timestamp es la fecha que tiene el archivo 
# acceso Sun Sep 22 21:05:18 2024
print("acceso",  ctime(archivo.stat().st_atime))
# Creacion Sun Sep 22 21:04:03 2024
print("Creacion",  ctime(archivo.stat().st_birthtime))
# Modificacion Sun Sep 22 21:15:15 2024
print("Modificacion",  ctime(archivo.stat().st_mtime))
from pathlib import Path    

path = Path("08-rutas")
# #existe?
# path.exists()
# #crear directorio / carpeta
# path.mkdir()
# # eliminar directorio
# path.rmdir()
# # renombrer
# path.rename("Santiago-feliz")

# Objeto generador "<generator object Path.iterdir at 0x000002422B1A3780>"
print(path.iterdir())


#08-rutas\01-path.py
# 08-rutas\02-directorios.py
for p in path.iterdir():
    print(p)

# comprension de listas
# La comprensión de listas crea una nueva lista que contiene solo los elementos p que cumplen la condición especificada (es decir, los que no son directorios).
#[WindowsPath('08-rutas/01-path.py'), WindowsPath('08-rutas/02-directorios.py')]
archivos = [p for p in path.iterdir() if not p.is_dir()]

# [WindowsPath('08-rutas/01-path.py')]
archivos = [p for p in path.glob("01-*.py")]
# [WindowsPath('08-rutas/01-path.py'), WindowsPath('08-rutas/02-directorios.py')]
archivos = [p for p in path.glob("**/*.py")]
#Recursivo
#  [WindowsPath('08-rutas/01-path.py'), WindowsPath('08-rutas/02-directorios.py')]
archivos = [p for p in path.rglob("*.py")]
print(archivos)
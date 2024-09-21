from pathlib import Path

# ROW STRING
# Path(r"C:\Archivos de programa\Minecreaft")
# # Ruta absoluta
# Path("/usr/bin")
# Path()
# Path.home()
# Path("one/__init__.py")

path = Path("hola-mundo/mi-archivo.py")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name,#mi-archivo.py -- NOMBRE DE ARCHIVO INCLUYENDO EXTENSION
    path.stem,#mi-archivo -- NOMBRE DEL ARCHIVO SIN EXTENSION
    path.suffix,#.py -- EXTENSION
    path.parent,#hola-mundo -- CARPETA PADRE
    path.absolute()#C:\Users\artur\Desktop\CoursePython\hola-mundo\mi-archivo.py  -- RUTA COMPLETA
)

p = path.with_name("chanchito.exe") #CAMBIO NMBRE DEL ARCHIVO
print(p)
p = path.with_suffix(".bat")#CAMBIO DE EXTENSION DEL ARCHIVO
print(p)
p = path.with_stem("feliz")#CAMBIO DE NOMBRE CARPETA PADRE
print(p)
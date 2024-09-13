#DE usuario importa guardar y pagar impuestos
import usuarios.acciones
from usuarios.acciones.utilidades import guardar, pagar_impuestos
from usuarios.acciones.crud import crud
#import usuarios.acciones
#from usuarios import acciones
import usuarios


# pagar_impuestos()#Pagando impuestos
# guardar()#Guardar
#usuarios,acciones.guardar()#Guardar


#['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'acciones']
print(dir(usuarios))

#<module 'usuarios.acciones' from 'c:\\Users\\artur\\Desktop\\CoursePython\\07-modulos\\usuarios\\acciones\\__init__.py'>
print(usuarios.acciones)
print(usuarios.__name__)
print(usuarios.__package__)
print(usuarios.__path__)
print(usuarios.__file__)
#LAS FILAS LLEVAN EL NOBRE FIFO
#FI -> FIRST IN  // PRIMERO ENTRA
#FO -> FIRST OUT // PRIMERO SALE

from collections import deque

fila = deque([1,2])
#agregar
# fila.append(3)
# fila.append(4)
# fila.append(5)
# print(fila) #deque([1, 2, 3, 4, 5])
# eliminar
fila.popleft()
fila.popleft()

if not fila:
    print("fila vacia")

print(fila)
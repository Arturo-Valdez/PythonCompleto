import os
from pathlib import Path
import sys


def cli(args):
    if len(args) == 1:
        print("No se pasaron argumentos")
        return
    if len(args) != 3:
        print("Se necesitan 2 argumentos")

    origen = args[1]
    o = Path(origen)
    if not o.exists():
        print("Origen no existe")
        return
    
    destino = args[2]
    d = Path(destino)
    if d.exists():
        print("El destino no puede existir")
        return
    os.rename(str(origen), str(destino))
    print("Archivo renombrado con exito")


# python 11-paquetes-nativos/05-cli.py 11-paquetes-nativos/lala-destino.md 11-paquetes-nativos/ejemplo/lala-destino2.md
cli(sys.argv)
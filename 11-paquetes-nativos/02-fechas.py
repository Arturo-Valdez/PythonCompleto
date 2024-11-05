# import time

# #ESTE NUMERO ES UN TIMESTAMP - OCURRIDO DESDE EL 1ERO DE ENERO DE 1970
# #  FECHA GENERADA POR UTC COORDINATED UNIVERSAL TIME EN INGLATERRA

# #1730846794.451408
# print(time.time())


from datetime import datetime
#PASAR AÑO - MES - DIA
fecha = datetime(2024,11,5)
fecha2 = datetime(2024,2,5)

ahora = datetime.now()


print(ahora)#2024-11-05 16:53:28.205100
print(fecha)#2024-11-05 00:00:00

#ORDENAR CON DIRECTIPS
fechaStr = datetime.strptime("2023-01-03" , "%Y-%m-%d")
print(fechaStr)#2023-01-03 00:00:00


# FORTMATIAR FECHA
print(fecha.strftime("%Y.%m-%d"))#2024.11-05

print(
    fecha.year,
    fecha.month,
    fecha.day,
    fecha.hour,
    fecha.minute
)#2024 11 5 0 0
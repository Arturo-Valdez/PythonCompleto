from datetime import datetime, timedelta

#Se agrega na semana extra
fecha1 = datetime(2024, 11, 1) + timedelta(weeks=1)
fecha2 = datetime(2024, 12, 1)

#OPTENER EL RANGO DE SEPARACION DE DISTINTAS FECHAS
# VARIABLE TIMEDELTA
delta = fecha2 - fecha1

print(delta)#30 days, 0:00:00.


print("dias", delta.days)#dias 30
print("segundos", delta.seconds)#segundos 0
print("microsegundos", delta.microseconds)#microsegundos 0
print("total de segundos", delta.total_seconds())#total de segundos 2592000.0

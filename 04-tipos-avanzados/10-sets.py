#SERT SIGNIFICA GRUPO O CONJUNTO

#SET SE ENCARGA EN ELIMINAR DATOS DUPLICADOS
primerSet = {1, 1, 2, 2, 3, 4}
print(primerSet)#{1, 2, 3, 4}

primerSet.add(5)
primerSet.remove(3)
print(primerSet)#{1, 2, 4, 5}


segundoSet = [3, 4, 5]

# Se trasnforma una lista en un set
segundoSet = set(segundoSet)
print(segundoSet)#{3, 4, 5}

#UNION
#SE REALIZA LA UNION DE AMBOS SETS
print(primerSet | segundoSet)#{1, 2, 3, 4, 5}

#INTERSECCION
#SE REALIZA INTESECCION DONDE SOLO REGRESA LOS VALORES
#QUE SE ENCUENTRA PARECIDOS DEL PRIMER Y SEGUNDO SET
#primerSet = {1, 1, 2, 2, 3, 4}
#segundoSet = [3, 4, 5]
print(primerSet & segundoSet)#{4, 5}


#DIFERENCIA
#SACA LA DIFERENCIA LOS VALORES PARECIDOS SE ELIMINAN
#QUEDANDO SOLO LOS IMPARES
#primerSet = {1, 1, 2, 2, 3, 4}
#segundoSet = [3, 4, 5]
print(primerSet - segundoSet)#{1, 2}


#DIFERENCIA SIMETRICA
#primerSet = {1, 1, 2, 2, 3, 4}
#segundoSet = [3, 4, 5]
print(primerSet ^ segundoSet)#{1, 2, 3}

#NO SE PUEDEN MODIFICAR DATOS PERO SI AGREGAR Y ELIMINAR
if 5 in segundoSet:
    print("Hola mundo")#Hola mundo


animal = "  chanCHio feliz  "

#funciones
print(animal.upper()) #Transformar variable en mayusculas
print(animal.lower())#Transformar variable en minusculas
print(animal.capitalize())#Transformar el primer caracter (sea espacio) y la vuelve mayusculas y las demas minusculas
print(animal.strip().capitalize())#Elimina los espacios excedidos de inicio y los finales y ransformar el primer caracter (sea espacio) y la vuelve mayusculas y las demas minusculas
print(animal.title())#Transformar la primera letra de todas las palabras en mayusculas y demas minusculas
print(animal.strip())#Elimina los espacios excedidos de inicio y los finales
print(animal.rstrip())#Elimina los espacios excedidos del lado derecho
print(animal.lstrip())#Elimina los espacios excedidos del lado izquierdo
print(animal.find("CH"))#Localiza en que indice se encuentra CH, en caso de no estar mostrara un -1
print(animal.replace("nCH", "j"))#Remplaza las letras CH por j
print("nCH" in animal)#Devuelve un Boolean si los caracteres se encuentran en animal(Si se encuentra es true, sino es False)
print("nCH" not in animal)#Devuelve un Boolean si los caracteres no se encuentran en animal (si no se encuentran es True, si se encuentran es False)


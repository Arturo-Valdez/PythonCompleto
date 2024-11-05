import random
import string


lista = [1,2,3,4,5,6,7,8,9]
lista2 = [1,2,3,4,5,6,7,8,9]
random.shuffle(lista)
print(
    random.random(),#CREAR NUMEROS ALEATORIOS DEL 0 A 1 CON DECIMALES #0.9510690557277816
    random.randint(1,10),#CREAR NUMEROS ALEATORIOS DEL 1 AL 10 #10
    lista,#MEZCLAR NUMEROS DE UNA LISTA #[3, 7, 9, 5, 2, 6, 1, 4, 8]
    random.choice(lista2),#OBTENER UN VALOR DE UNA LISTA #8
    random.choices(lista2, k=3),#OBTENER CANTIDAD DE N VALORES DE UNA LISTA #[8, 1, 9]
    random.choices("abcdfghi.,123", k=3),#CREAR UNA LISTA DONDE OBTENEMOS N VALORES CON UN STRING #['3', '1', 'g']
    "".join(random.choices("abcdfghi.,123", k=3))#obtener un string con N valores tipo contraseña #hcb
    )

#La variable chars contiene todas las letras del alfabeto en minúsculas y mayúsculas. string.ascii_letters es una constante en el módulo string que incluye todas las letras del alfabeto en inglés (de 'a' a 'z' y de 'A' a 'Z').
chars = string.ascii_letters
# La variable digitos contiene los caracteres numéricos del 0 al 9. string.digits es otra constante del módulo string que incluye los dígitos del 0 al 9.
digitos = string.digits
# Esta línea utiliza la función random.choices(), que selecciona aleatoriamente caracteres de una secuencia. La secuencia que se usa en este caso es la concatenación de chars (letras) y digitos (números), es decir, todos los caracteres alfabéticos y numéricos.
# La opción k=12 indica que se seleccionarán 12 caracteres al azar.
seleccion = random.choices(chars + digitos, k=12)

# La función join() se usa para combinar los caracteres seleccionados (que están en una lista) en una sola cadena de texto (string). Así, la variable password contendrá la contraseña generada, que será una secuencia aleatoria de 12 caracteres.
password = "".join(seleccion)
print(password)
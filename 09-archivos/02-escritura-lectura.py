from pathlib import Path

# UTF-8 es una codificación de caracteres que puede representar todos los caracteres del estándar Unicode. Aquí te explico algunos puntos clave sobre UTF-8:



archivo = Path("09-archivos/archivo-prueba.txt")

# Lee el contenido de un archivo de texto.
# lee el contenido del archivo como una cadena de texto utilizando la codificación UTF-8.
# .split("\n") divide el contenido del archivo en una lista de líneas, usando el carácter de nueva línea (\n) como delimitador.
texto = archivo.read_text("utf-8").split("\n")


#  línea inserta la cadena "hola mundo!" al principio de la lista texto, que ahora tiene una línea adicional.
texto.insert(0, "hola mundo!")

# une la lista de líneas en una sola cadena, insertando un carácter de nueva línea entre cada línea.
archivo.write_text("\n".join(texto), "utf-8")


print(texto)
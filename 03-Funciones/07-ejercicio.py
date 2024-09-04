# Elimina todos los espacios y vuelve minusculas todas las letras
def no_space(texto):
    texto_blanco = ""
    for char in texto:
        if char != " ":
            texto_blanco += char
    return texto_blanco.lower()

# Voltea todas las letras en posicion contraria
def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves

# Comparacion de si la palabra es un palindromo
def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    if texto == texto_al_reves:
        return True
    else:
        return False


print("Amo la paloma ", es_palindromo("a m o la paloma  "))
print("Hola Muno MYnasJ ", es_palindromo("Hola Muno MYnasJ"))

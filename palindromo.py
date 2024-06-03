def es_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]
def verificar_palindromo(texto):
    if es_palindromo(texto):
        print(f"'{texto}' es un palíndromo.")
    else:
        print(f"'{texto}' no es un palíndromo.")
entrada = input("Ingresa una palabra o frase para verificar si es un palíndromo: ")
verificar_palindromo(entrada)

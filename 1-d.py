'''
Escribe un programa que pida al usuario que ingrese una letra del
alfabeto y determine si es una vocal o una consonante.
'''

def tipo_letra(letra):
    if letra.lower() in "aeiou":
        return "Es una vocal"
    else:
        return "Es una consonante"

letra = input("Ingresa una letra: ")
resultado = tipo_letra(letra)
print(resultado)
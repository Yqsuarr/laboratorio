'''
Escribe un programa que pida al usuario que
ingrese una cadena de texto y luego cuente cuántas veces aparece una letra específica en la cadena.
'''

def contar_letra(cadena, letra):
    contador = 0
    i = 0
    while i < len(cadena):
        if cadena[i] == letra:
            contador += 1
        i += 1
    return contador

cadena = input("Ingresa una cadena: ")
letra = input("Ingresa una letra: ")
resultado = contar_letra(cadena, letra)
print("La letra aparece:", resultado, "veces")
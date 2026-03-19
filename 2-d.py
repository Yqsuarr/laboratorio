'''
Escribe un programa que pida al usuario que
ingrese una palabra y luego muestre cada letra de la palabra en una línea separada.
'''

def mostrar_letras(palabra):
    for letra in palabra:
        print(letra)

palabra = input("Ingresa una palabra: ")
mostrar_letras(palabra)
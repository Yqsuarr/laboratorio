'''
Juego de adivinanzas: Escribe un programa que genere un arreglo de palabras.
El programa debe elegir una palabra aleatoria y mostrar la primera letra.
El usuario debe adivinar la palabra ingresando una letra a la vez.
Si la letra ingresada es correcta, el programa debe mostrar la letra en la posición correspondiente.
Si la letra es incorrecta, el programa debe mostrar un mensaje de error.
El usuario gana cuando ha adivinado todas las letras de la palabra.
'''

import random


def elegir_palabra():
    palabras = ["zapallo", "tomate", "palta"]
    return random.choice(palabras)


def inicializar(palabra):
    adivinada = []

    for i in range(len(palabra)):
        adivinada.append("_")

    adivinada[0] = palabra[0]

    return adivinada


def actualizar(palabra, adivinada, letra):
    acierto = False

    for i in range(len(palabra)):
        if palabra[i] == letra:
            adivinada[i] = letra
            acierto = True

    return acierto


def jugar(palabra):
    adivinada = inicializar(palabra)
    terminado = False

    print("Palabra:", " ".join(adivinada))

    while terminado == False:
        letra = input("Ingresa una letra: ")

        acierto = actualizar(palabra, adivinada, letra)

        if acierto == True:
            print("Correcto:", " ".join(adivinada))
        else:
            print("Incorrecto")

        if "_" not in adivinada:
            terminado = True

    print("Ganaste. La palabra era:", palabra)


def main():
    palabra = elegir_palabra()
    jugar(palabra)


main()
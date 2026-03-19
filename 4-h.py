'''
Palabras cruzadas: Escribe un programa que genere una
palabra aleatoria y la muestre con una letra oculta en cada posición.
El usuario debe ingresar una letra para cada posición oculta.
Si la letra ingresada es correcta, el programa debe mostrar
la letra en la posición correspondiente. Si la letra es incorrecta,
el programa debe mostrar un mensaje de error. El usuario gana cuando ha adivinado todas las letras de la palabra.
'''

import random


def elegir_palabra():
    palabras = ["python", "codigo", "juego"]
    return random.choice(palabras)


def crear_oculta(palabra):
    oculta = []

    for i in range(len(palabra)):
        oculta.append("_")

    return oculta


def actualizar_oculta(palabra, oculta, letra):
    acierto = False

    for i in range(len(palabra)):
        if palabra[i] == letra:
            oculta[i] = letra
            acierto = True

    return acierto


def juego(palabra):
    oculta = crear_oculta(palabra)
    terminado = False

    while terminado == False:
        letra = input("Ingresa una letra: ")

        acierto = actualizar_oculta(palabra, oculta, letra)

        if acierto == True:
            print("Correcto:", " ".join(oculta))
        else:
            print("Incorrecto")

        if "_" not in oculta:
            terminado = True

    print("Ganaste. La palabra era:", palabra)


def main():
    palabra = elegir_palabra()
    juego(palabra)


main()
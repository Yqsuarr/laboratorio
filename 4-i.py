'''
Juego de memoria: Escribe un programa que genere un arreglo de números aleatorios.
El programa debe mostrar el arreglo por unos segundos y luego ocultar los números.
El usuario debe ingresar los números en el orden correcto.
Si el usuario ingresa los números en el orden correcto, gana.
Si el usuario se equivoca en algún número, pierde.
'''

import random
import time


def generar_lista():
    numeros = []

    for i in range(5):
        numeros.append(random.randint(1, 9))

    return numeros


def mostrar_lista(numeros):
    print("Memoriza estos numeros:")
    print(numeros)

    time.sleep(3)
    print("\n" * 30)


def pedir_respuesta():
    texto = input("Ingresa los numeros en orden: ")
    partes = texto.split()

    respuesta = []

    for p in partes:
        respuesta.append(int(p))

    return respuesta


def verificar(respuesta, numeros):
    return respuesta == numeros


def main():
    numeros = generar_lista()

    mostrar_lista(numeros)

    respuesta = pedir_respuesta()

    if verificar(respuesta, numeros):
        print("Ganaste")
    else:
        print("Perdiste. Eran:", numeros)


main()
'''
Adivina el número: Escribe un programa que genere un número aleatorio
entre 1 y 100. El usuario debe adivinar el número y el programa debe decir si el número
ingresado es mayor o menor al número generado. El usuario gana cuando adivina el número.
'''

import random


def generar_numero():
    return random.randint(1, 100)


def jugar(numero):
    adivinado = False

    while adivinado == False:
        intento = int(input("Adivina el numero: "))

        if intento < numero:
            print("El numero es mayor")

        elif intento > numero:
            print("El numero es menor")

        else:
            print("Ganaste")
            adivinado = True


def main():
    numero = generar_numero()
    jugar(numero)


main()
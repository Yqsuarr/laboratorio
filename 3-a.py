'''
Escribe un programa que pida al usuario que adivine un número secreto generado aleatoriamente.
El programa debe dar pistas al usuario diciéndole si el número ingresado es mayor o menor que el número secreto.
'''

import random

def juego_adivinar():
    secreto = random.randint(1, 100)
    intento = 0

    while intento != secreto:
        intento = int(input("Adivina el numero: "))
        if intento < secreto:
            print("El numero es mayor")
        elif intento > secreto:
            print("El numero es menor")

    return "Adivinaste"

resultado = juego_adivinar()
print(resultado)
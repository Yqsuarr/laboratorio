'''
Piedra, papel o tijeras: Escribe un programa que permita al
usuario jugar piedra, papel o tijeras contra el programa.
El usuario debe ingresar su elección y el programa debe generar
una elección aleatoria. El programa debe determinar quién gana la partida y mostrar el resultado.
'''

import random


def obtener_jugada_usuario():
    jugada = input("Elige piedra, papel o tijera: ")
    return jugada.lower()


def obtener_jugada_pc():
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)


def determinar_ganador(usuario, pc):
    if usuario == pc:
        return "Empate"

    if usuario == "piedra" and pc == "tijera":
        return "Ganaste"

    if usuario == "tijera" and pc == "papel":
        return "Ganaste"

    if usuario == "papel" and pc == "piedra":
        return "Ganaste"

    return "Perdiste"


def main():
    usuario = obtener_jugada_usuario()
    pc = obtener_jugada_pc()

    print("La PC eligio:", pc)

    resultado = determinar_ganador(usuario, pc)

    print(resultado)


main()
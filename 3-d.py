'''
Escribe un programa que simule una carrera entre dos corredores.
Cada corredor avanza un número de metros generado aleatoriamente en cada iteración del ciclo.
El programa debe mostrar quién ganó la carrera y en cuántos segundos.
'''

import random

def carrera():
    corredor1 = 0
    corredor2 = 0
    segundos = 0

    while corredor1 < 100 and corredor2 < 100:
        corredor1 += random.randint(1, 10)
        corredor2 += random.randint(1, 10)
        segundos += 1

    if corredor1 > corredor2:
        return f"Gano el corredor 1 en {segundos} segundos"
    elif corredor2 > corredor1:
        return f"Gano el corredor 2 en {segundos} segundos"
    else:
        return f"Empate en {segundos} segundos"

resultado = carrera()
print(resultado)
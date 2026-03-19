'''
Escribe un programa que lea un arreglo de números enteros
y luego muestre cuántos elementos del arreglo son pares.
'''

def leer_numeros():
    texto = input("Ingresa numeros separados por espacios: ")
    partes = texto.split()

    numeros = []
    for p in partes:
        numeros.append(int(p))

    return numeros


def contar_pares(numeros):
    cantidad = 0

    for n in numeros:
        if n % 2 == 0:
            cantidad = cantidad + 1

    return cantidad


def main():
    numeros = leer_numeros()
    resultado = contar_pares(numeros)

    print("Cantidad de pares:", resultado)


main()
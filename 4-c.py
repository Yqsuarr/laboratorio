'''
Escribe un programa que lea un arreglo de
números enteros y luego muestre el elemento mínimo del arreglo.
'''

def leer_numeros():
    texto = input("Ingresa numeros separados por espacios: ")
    partes = texto.split()

    numeros = []
    for p in partes:
        numeros.append(int(p))

    return numeros


def calcular_minimo(numeros):
    minimo = numeros[0]

    for n in numeros:
        if n < minimo:
            minimo = n

    return minimo


def main():
    numeros = leer_numeros()
    resultado = calcular_minimo(numeros)

    print("Minimo:", resultado)


main()
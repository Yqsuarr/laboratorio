'''
Escribe un programa que lea un arreglo de números enteros
y luego muestre el elemento máximo del arreglo.
'''

def leer_numeros():
    texto = input("Ingresa numeros separados por espacios: ")
    partes = texto.split()

    numeros = []
    for p in partes:
        numeros.append(int(p))

    return numeros


def calcular_maximo(numeros):
    maximo = numeros[0]

    for n in numeros:
        if n > maximo:
            maximo = n

    return maximo


def main():
    numeros = leer_numeros()
    resultado = calcular_maximo(numeros)

    print("Maximo:", resultado)


main()
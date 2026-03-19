'''
Escribe un programa que lea un arreglo de números enteros
y luego muestre la media (promedio) de los elementos del arreglo.
'''

def leer_numeros():
    texto = input("Ingresa numeros separados por espacios: ")
    partes = texto.split()

    numeros = []
    for p in partes:
        numeros.append(int(p))

    return numeros


def calcular_promedio(numeros):
    suma = 0

    for n in numeros:
        suma = suma + n

    promedio = suma / len(numeros)

    return promedio


def main():
    numeros = leer_numeros()
    resultado = calcular_promedio(numeros)

    print("Promedio:", resultado)


main()
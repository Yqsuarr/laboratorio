'''
Escribe un programa que lea un arreglo de números enteros
y luego muestre la suma de todos los elementos del arreglo.
'''

numeros = list(map(int, input("Ingresa números separados por espacios: ").split()))

suma = sum(numeros)

print("La suma es:", suma)
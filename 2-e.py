'''
Escribe un programa que pida al usuario que ingrese un
número y luego muestre la suma de los números impares desde 1 hasta ese número.
'''

def suma_impares(n):
    suma = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            suma += i
    return suma

n = int(input("Ingresa un numero: "))
resultado = suma_impares(n)
print("La suma de impares es:", resultado)
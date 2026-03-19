'''
Escribe un programa que calcule la suma de los primeros
100 números naturales (es decir, 1 + 2 + 3 + ... + 100).
'''

def suma_100():
    suma = 0
    for i in range(1, 101):
        suma += i
    return suma

resultado = suma_100()
print("La suma es:", resultado)
'''
Escribe un programa que pida al usuario que ingrese números enteros positivos
y luego calcule la suma de todos los números ingresados hasta que el usuario ingrese un número negativo.
'''

def suma_hasta_negativo():
    suma = 0
    numero = 0

    while numero >= 0:
        numero = int(input("Ingresa un numero (negativo para salir): "))
        if numero >= 0:
            suma += numero

    return suma

resultado = suma_hasta_negativo()
print("La suma total es:", resultado)
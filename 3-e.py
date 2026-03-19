'''
Escribe un programa que pida al usuario que ingrese números enteros positivos
y luego calcule el producto de todos los números ingresados hasta que el usuario ingrese un número negativo.
'''

def producto_hasta_negativo():
    producto = 1
    numero = 0

    while numero >= 0:
        numero = int(input("Ingresa un numero (negativo para salir): "))
        if numero >= 0:
            producto *= numero

    return producto

resultado = producto_hasta_negativo()
print("El producto total es:", resultado)
'''
Escribe un programa que pida al usuario que ingrese
dos números y determine cuál es el número más grande.
'''

def numero_mayor(a, b):
    if a > b:
        return f"El numero mayor es {a}"
    elif b > a:
        return f"El numero mayor es {b}"
    else:
        return "Los numeros son iguales"

a = int(input("Ingresa el primer numero: "))
b = int(input("Ingresa el segundo numero: "))
resultado = numero_mayor(a, b)
print(resultado)
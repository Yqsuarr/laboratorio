'''
Escribe un programa que lea un número entero
y determine si es positivo, negativo o cero.
'''

def determinar_signo(numero):
    if numero > 0:
        return "El numero es positivo."
    elif numero < 0:
        return "El numero es negativo."
    else:
        return "El numero es cero."
numero = int(input("Ingresa un numero entero: "))
resultado = determinar_signo(numero)
print(resultado)
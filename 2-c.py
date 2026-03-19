'''
Escribe un programa que muestre las tablas de multiplicar del 1 al 10.
'''

def tablas():
    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i} x {j} = {i*j}")
        print("")

tablas()
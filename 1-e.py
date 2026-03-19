'''
Escribe un programa que pida al usuario que ingrese un número del 1 al 7 y determine a qué día
de la semana corresponde (1 es lunes, 2 es martes, etc.).
Si el número no está en ese rango, el programa debe mostrar un mensaje de error.
'''

def dia_semana(numero):
    dias = {
        1: "Lunes",
        2: "Martes",
        3: "Miercoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sabado",
        7: "Domingo"
    }
    return dias.get(numero, "Error: numero fuera de rango")

numero = int(input("Ingresa un numero del 1 al 7: "))
resultado = dia_semana(numero)
print(resultado)
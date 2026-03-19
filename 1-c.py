'''
Escribe un programa que pida al usuario que ingrese su edad
y determine si es mayor de edad (18 años o más) o menor de edad.
'''

def determinar_edad(edad):
    if edad >= 18:
        return "Es mayor de edad"
    else:
        return "Es menor de edad"

edad = int(input("Ingresa tu edad: "))
resultado = determinar_edad(edad)
print(resultado)
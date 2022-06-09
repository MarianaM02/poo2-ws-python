"""
Escribir una función que reciba una cadena de caracteres muestre por pantalla la
frecuencia de aparición de cada letra. Por ejemplo:
frecuencias("hola como estas..."); // debe mostrar por pantalla:
a: 2
c: 1
e: 1
h: 1
l: 1
m: 1
o: 3
s: 2
t: 1
"""

def frecuenciaCaracteres(cadena):
    cadena = cadena.lower().replace(" ", "")
    frecuencia = {}
    for caracter in cadena:
        if caracter in frecuencia:
            frecuencia[caracter] += 1
        else:
            frecuencia[caracter] = 1
    return frecuencia

print(frecuenciaCaracteres(input("Ingrese una cadena de caracteres: ")))
"""
Escribir una función que reciba dos arreglos ​a1 y ​a2​, de enteros ordenados de
mayor a menor e intercale los elementos de los arreglos que recibe en un nuevo
arreglo, tal que el arreglo resultante también esté ordenado. Por ejemplo:
a1 = [-5, 0, 0, 1, 5]
a2 = [-10, 0, 7]
resultado = [-10, -5, 0, 0, 0, 1, 5, 7]
"""

def intercalarArreglos(a1, a2):
    resultado = []
    i = 0
    j = 0
    while i < len(a1) and j < len(a2):
        if a1[i] > a2[j]:
            resultado.append(a2[j])
            j += 1
        else:
            resultado.append(a1[i])
            i += 1
    while i < len(a1):
        resultado.append(a1[i])
        i += 1
    while j < len(a2):
        resultado.append(a2[j])
        j += 1
    return resultado

print(intercalarArreglos([-5, 0, 0, 1, 5], [-10, 2, 7]))
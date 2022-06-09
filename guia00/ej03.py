"""
Escribir una función que reciba un arreglo de enteros y devuelva ​true si el arreglo
está ordenado de mayor a menor y ​false​ si está desordenado.
"""


def estaOrdenada(lista):
    anterior = lista[0]
    for i in range(1, len(lista)):
        if not (anterior <= lista[i]):
            return False
        anterior = lista[i]

    return True


lista = [0, 3, 7, 8, 15]
print(estaOrdenada(lista))

lista = [0, 3, 8, 7, 15]
print(estaOrdenada(lista))

lista = [0, 3, 3, 7, 15]
print(estaOrdenada(lista))

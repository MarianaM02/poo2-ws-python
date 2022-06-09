"""
Escribir un método que reciba como parámetro una matriz cuadrada de números
reales y devuelva true (o false), si todos los elementos (fuera de la diagonal
principal) están por encima de la media de los elementos de la diagonal principal.
"""


def encimaMediaDiagonal(arr):
    tamanio = len(arr)
    media = 0
    for i in range(tamanio):
        media += arr[i][i]
    media /= tamanio

    for i in range(tamanio):
        for j in range(tamanio):
            if i != j:
                if arr[i][j] <= media:
                    return False
    return True


print(encimaMediaDiagonal([[1,2,1],[2,1,1],[1,1,2]]))
print(encimaMediaDiagonal([[1,2,2],[2,1,2],[2,2,1]]))
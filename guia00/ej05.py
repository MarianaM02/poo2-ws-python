"""
Escribir una función que reciba dos matrices de ​NxN y devuelva la suma de las
mismas. Podemos considerar que las matrices se representan como un arreglo
bidimensional.
"""


def sumaMatrices(m1, m2):
    resultado = []
    for i in range(len(m1)):
        resultado.append([])
        for j in range(len(m1[i])):
            resultado[i].append(m1[i][j] + m2[i][j])
    return resultado


print(sumaMatrices([[1,2,1],[2,1,1],[1,1,2]], [[1,1,1],[1,1,1],[1,1,1]]))

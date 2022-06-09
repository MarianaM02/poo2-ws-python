"""
2. Escribir una función que calcule la suma de los múltiplos de 3 y 5, mayores o
iguales que 0 y menores que un parámetro ​n​. Por ejemplo la llamada:
sumaMultiplos(10); // devuelve 23 (3+5+6+9)
sumaMultiplos(16); // devuelve 60 (3+5+6+9+10+12+15)
"""


def sumaMultiplos3y5(n):
    suma = 0
    for i in range(0, n):
        if i % 3 == 0 or i % 5 == 0:
            suma += i
    return suma


print(sumaMultiplos3y5(10))
print(sumaMultiplos3y5(16))

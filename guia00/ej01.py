# 1. Escribir una función que reciba un número ​n y devuelva ​true si ​n es primo o ​false en caso ​contrario
import math


def esPrimo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    raiz = int(math.sqrt(n))
    for i in range(2, raiz):
        resto = n % i
        if resto == 0:
            return False
    return True


print(esPrimo(int(input())))

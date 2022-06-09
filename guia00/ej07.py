"""
 Escribir un programa que genere un número entero aleatorio entre ​0 y ​1000 y le
pida al usuario que lo adivine, si el usuario acierta debe responder con la cantidad
de intentos y si el usuario no quiere continuar adivinando debe ingresar ​'*' y
entonces debe mostrar cuál era el número.
"""
from random import randint


def adivinarNumero():
    a = randint(0, 1000)
    n = input("Adivine el numero: ")
    while n != "*":
        if int(n) != a:
            n = input("Incorrecto. Intente nuevamente: ")
        else:
            print("Correcto! El numero era ",a)
            return
    print("Otra vez será! El numero era ",a)
    

adivinarNumero()

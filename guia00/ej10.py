"""
Escribir una función ​consonantes que recibe una cadena de caracteres y devuelve
la cadena que resulta de eliminar todas las vocales de la cadena recibida. Por
ejemplo:
consonantes("hola como estas"); // devuelve "hl cm sts"
"""
import re

def eliminarVocales(cadena):
    return "".join(re.findall("[^aeiouAEIOUáéíóúÁÉÍÓÚ]", cadena))


print(eliminarVocales("hola como estas"))
print(eliminarVocales("Escribir una función ​consonantes que recibe una cadena de caracteres devuelve la cadena que resulta de eliminar todas las vocales de la cadena recibida"))
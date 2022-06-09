"""
Una señal de audio digitalizada puede representarse como un arreglo de enteros,
que oscilan entre ‘0’ (silencio) y ‘65536’ (tono agudo).
Se desea construir un software que dada la señal, aplique un filtro pasa-banda
definido por dos tonos (inferior y superior), que deja en silencio todo valor fuera de
ese rango. El resultado debe compactarse, eliminando los silencios generados por
este filtro.
Nota 1: Es estrictamente necesario aplicar el filtro primero, y luego compactar la
señal.
Nota 2: No debe perderse la señal original.
"""


class SenialAudio:
    def __init__(self, arr):
        self.senial = list(arr)


class Filtro:
    def __init__(self, min, max):
        self.MIN = min
        self.MAX = max

    def filtroPasaBanda(self, arr):
        nueva = list(arr)
        for i in range(len(nueva)):
            if nueva[i] < self.MIN or nueva[i] > self.MAX:
                nueva[i] = 0
        return SenialAudio(self.comprimir(nueva))

    def comprimir(self, arr):
        nueva = []
        for i in arr:
          if i != 0:
            nueva.append(i)
        return nueva

senAudio = SenialAudio([2,7,4,5,6,9,2])
filtro = Filtro(3, 6)
nuevoAudio = filtro.filtroPasaBanda(senAudio.senial)
print(nuevoAudio.senial)
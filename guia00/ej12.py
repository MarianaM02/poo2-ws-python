"""
Implementar la clase Hotel tal que tenga operaciones para:
a. Crearla con la cantidad de habitaciones que tiene.
b. Ocupar una habitación disponible indicando la cantidad de
personas mayores y menores (máximo 8 en total) que la ocuparán.
void ocuparHabitacionCon(int mayores, int menores)
c. Devolver la cantidad total de personas que ocupan todas las
habitaciones del hotel.
d. Devolver la cantidad de habitaciones que están ocupadas por
tantos mayores como los indicados por parámetro.
int contarHabitacionesCon(int mayores)
e. Devolver un arreglo de enteros de longitud 9, tal que en la
posición i del arreglo se guarde la cantidad de habitaciones
con i personas.
"""


class Hotel:
    def __init__(self, nro):
        self.cantHabitaciones = nro
        self.ocupadas = 0
        self.habitaciones = []
        for i in range(0, nro):
            self.habitaciones.append([0, 0])

    def ocuparHabitacionCon(self, mayores, menores):
        if self.ocupadas == self.cantHabitaciones:
            return False

        if mayores+menores >= 8 or mayores < 1 or menores < 0:
            return False

        for hab in self.habitaciones:
            if sum(hab) == 0:
                hab[0] = mayores
                hab[1] = menores
                self.ocupadas += 1
                return True
        return False

    def cantidadHuespedes(self):
        #return sum(sum(huespedes) for huespedes in self.habitaciones)
        return sum(sum(self.habitaciones, []))

    def contarHabitacionesConMayores(self, nro):
        total = 0
        for hab in self.habitaciones:
            if hab[0] == nro:
                total += 1
        return total

    def contarPersonasPorHabitacion(self):
        cantPersonas = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for hab in self.habitaciones:
            cantPersonas[sum(hab)] += 1
        return cantPersonas


hotel = Hotel(5)

print(hotel.ocuparHabitacionCon(2, 1))
print(hotel.ocuparHabitacionCon(2, 8))
print(hotel.ocuparHabitacionCon(0, 1))
print(hotel.ocuparHabitacionCon(2, 1))
print(hotel.ocuparHabitacionCon(2, 1))
print(hotel.ocuparHabitacionCon(4, 1))
print(hotel.ocuparHabitacionCon(3, 1))
print(hotel.ocuparHabitacionCon(2, 1))
print(hotel.ocuparHabitacionCon(2, 1))

print(hotel.cantidadHuespedes())
print(hotel.habitaciones)
print(hotel.contarHabitacionesConMayores(3))
print(hotel.contarHabitacionesConMayores(2))
print(hotel.contarHabitacionesConMayores(5))
print(hotel.contarPersonasPorHabitacion())

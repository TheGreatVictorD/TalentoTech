"""
En la composición, una clase contiene objetos de
otra clase y es responsable de su ciclo de vida
"""


class Casa:
    def __init__(self, direccion):
        self.direccion = direccion
        self.habitaciones = []  # Lista de habitaciones

    def agregar_habitacion(self, tipo):
        nueva_habitacion = Habitacion(tipo)
        self.habitaciones.append(nueva_habitacion)
        return nueva_habitacion

    def imprimir_habitaciones(self):
        for habitacion in self.habitaciones:
            print(habitacion)


class Habitacion:
    def __init__(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return self.tipo


# Composición
mi_casa = Casa("Calle ABC")
habitacion_principal = mi_casa.agregar_habitacion("Dormitorio")
mi_casa.imprimir_habitaciones()

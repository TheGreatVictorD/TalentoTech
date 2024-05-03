"""
En una asociación simple, una clase tiene una referencia a otra pero no controla
su ciclo de vida ni tiene responsabilidades sobre ella más allá de la referencia.
"""


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


class Libro:
    def __init__(self, titulo):
        self.titulo = titulo

    def __str__(self):
        return self.titulo


# Asociación simple
persona = Persona("Juan")
libro = Libro("Python Programming")
persona.libro_actual = libro  # La persona tiene una referencia al libro que está leyendo
print(f'libros:\n'
      f'    -{persona.libro_actual}')

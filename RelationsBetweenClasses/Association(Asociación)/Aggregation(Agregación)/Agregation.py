"""
En la agregación, una clase contiene objetos de otra clase,
pero estos objetos pueden existir independientemente.
"""


class Universidad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []  # Lista de estudiantes

    def imprimiendo_estudiante(self):
        print('Estudiantes:')
        for estudiante in self.estudiantes:
            print(f'    -{estudiante}')


class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


# Agregación
universidad = Universidad("Universidad XYZ")
estudiante1 = Estudiante("Maria")
universidad.estudiantes.append(estudiante1)  # La universidad tiene una lista de estudiantes
universidad.imprimiendo_estudiante()

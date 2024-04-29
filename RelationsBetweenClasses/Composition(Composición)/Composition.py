"""
En este ejemplo, la composición se da porque la clase Persona se compone de objetos de las clases
Cabeza y Cuerpo. Esto significa que Persona tiene una Cabeza y un Cuerpo como parte de su estado.

En términos más simples, puedes pensar en la composición como una “relación de tiene”. En este caso,
una Persona tiene una Cabeza y tiene un Cuerpo.

Por ejemplo, cuando creas un objeto Persona, también creas un objeto Cabeza y un objeto Cuerpo que son
parte de la Persona. Estos objetos Cabeza y Cuerpo existen dentro del objeto Persona y se utilizan para
formar una entidad más compleja.

Es importante destacar que en una relación de composición, si el objeto contenedor (en este caso, Persona)
se destruye, entonces también se destruyen sus partes (Cabeza y Cuerpo).
"""


class Cabeza:
    def __init__(self, color_ojos):
        self.color_ojos = color_ojos


class Cuerpo:
    def __init__(self, altura):
        self.altura = altura


class Persona:
    def __init__(self, color_ojos, altura):
        self.cabeza = Cabeza(color_ojos)
        self.cuerpo = Cuerpo(altura)


persona = Persona("azules", 180)

print(persona.cabeza.color_ojos)  # Imprime: azules
print(persona.cuerpo.altura)  # Imprime: 180

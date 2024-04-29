"""
En este ejemplo, la herencia se da porque las clases Perro y Gato están heredando de la clase Animal.
Esto significa que Perro y Gato adquieren los atributos y métodos de la clase Animal.

En términos más simples, puedes pensar en la herencia como una “relación de tipo”. En este caso, tanto
un Perro como un Gato son tipos de Animal, por lo que heredan sus características.

Por ejemplo, tanto Perro como Gato heredan el método hablar() de Animal, pero cada uno proporciona su
propia implementación del método (el perro devuelve “Guau!” y el gato devuelve “Miau!”). Esto es un
ejemplo de polimorfismo, que es un concepto clave en la programación orientada a objetos y se facilita
mediante la herencia.
"""


class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        pass


class Perro(Animal):
    def hablar(self):
        return "Guau!"


class Gato(Animal):
    def hablar(self):
        return "Miau!"


perro = Perro("Fido")
gato = Gato("Whiskers")

print(perro.hablar())  # Imprime: Guau!
print(gato.hablar())  # Imprime: Miau!

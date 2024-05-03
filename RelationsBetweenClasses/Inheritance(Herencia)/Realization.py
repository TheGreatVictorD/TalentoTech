"""
La realización en herencia se da cuando una clase
implementa una interfaz definida por otra clase.
"""


# Interfaz (clase base abstracta)
class Forma:
    def calcular_area(self):
        raise NotImplementedError("Método calcular_area no implementado")


# Clase que realiza la interfaz
class Rectangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


# Crear un objeto Rectangulo
mi_rectangulo = Rectangulo(5, 10)

# Usar el método de la interfaz implementada
area_rectangulo = mi_rectangulo.calcular_area()
print(f"Área del rectángulo: {area_rectangulo}")

"""
En este ejemplo, la clase Rectangulo realiza la interfaz Forma, implementando 
el método calcular_area definido en la interfaz. La realización en herencia se 
utiliza para garantizar que las clases que implementan la interfaz tengan ciertos 
métodos definidos en la interfaz.
"""

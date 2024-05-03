"""
La generalización en herencia implica que una clase hija hereda atributos
y métodos de una clase padre y puede agregar o modificar su funcionalidad.
"""


# Clase padre o superclase
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def conducir(self):
        print(f"Conduciendo un vehículo {self.marca} {self.modelo}")


# Clase hija o subclase que generaliza
class Coche(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color

    def abrir_puertas(self):
        print("Puertas abiertas")


# Crear un objeto Coche
mi_coche = Coche("Toyota", "Corolla", "Rojo")

# Usar métodos de la clase padre y clase hija
mi_coche.conducir()  # Método heredado de la clase Vehiculo
mi_coche.abrir_puertas()  # Método propio de la clase Coche


"""
En este ejemplo, la clase Coche hereda de la clase Vehiculo. La clase Coche 
agrega un atributo color y un método abrir_puertas, además de usar el método 
conducir heredado de la clase Vehiculo. Esto muestra la generalización en 
herencia, donde la clase hija extiende la funcionalidad de la clase padre.
"""

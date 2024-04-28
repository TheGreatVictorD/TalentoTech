from abc import ABC, abstractmethod


# Clase Producto
class Pizza:
    def __init__(self):
        self.tipo = ""
        self.masa = ""
        self.salsa = ""
        self.ingredientes = []

    def agregar_tipo(self, tipo):
        self.tipo = tipo

    def agregar_masa(self, masa):
        self.masa = masa

    def agregar_salsa(self, salsa):
        self.salsa = salsa

    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def mostrar_pizza(self):
        print(f"Pizza {self.tipo} con masa {self.masa}, salsa {self.salsa} y los siguientes ingredientes:")
        for ingrediente in self.ingredientes:
            print(f"- {ingrediente}")
        print("¡Disfruta tu pizza!")


# Interfaz Builder
class PizzaBuilder(ABC):
    def __init__(self):
        self.pizza = Pizza()

    @abstractmethod
    def agregar_tipo(self):
        pass

    @abstractmethod
    def agregar_masa(self):
        pass

    @abstractmethod
    def agregar_salsa(self):
        pass

    @abstractmethod
    def agregar_ingrediente(self):
        pass

    def obtener_pizza(self):
        return self.pizza


# Constructores Concretos
class PizzaPepperoniBuilder(PizzaBuilder):
    def agregar_tipo(self):
        self.pizza.agregar_tipo("Pepperoni")

    def agregar_masa(self):
        self.pizza.agregar_masa("Regular")

    def agregar_salsa(self):
        self.pizza.agregar_salsa("Tomate")

    def agregar_ingrediente(self):
        self.pizza.agregar_ingrediente("Pepperoni")
        self.pizza.agregar_ingrediente("Queso")
        self.pizza.agregar_ingrediente("Orégano")


class PizzaVegetarianaBuilder(PizzaBuilder):
    def agregar_tipo(self):
        self.pizza.agregar_tipo("Vegetariana")

    def agregar_masa(self):
        self.pizza.agregar_masa("Integral")

    def agregar_salsa(self):
        self.pizza.agregar_salsa("Tomate")

    def agregar_ingrediente(self):
        self.pizza.agregar_ingrediente("Tomate")
        self.pizza.agregar_ingrediente("Pimiento")
        self.pizza.agregar_ingrediente("Cebolla")
        self.pizza.agregar_ingrediente("Aceitunas")


# Director
class Pizzeria:
    def __init__(self):
        self.builder = None

    def construir_pizza(self, builder):
        self.builder = builder
        self.builder.agregar_tipo()
        self.builder.agregar_masa()
        self.builder.agregar_salsa()
        self.builder.agregar_ingrediente()

    def obtener_pizza(self):
        return self.builder.obtener_pizza()


# Uso del Builder
pizzeria = Pizzeria()

pizza_pepperoni_builder = PizzaPepperoniBuilder()
pizzeria.construir_pizza(pizza_pepperoni_builder)
pizza_pepperoni = pizzeria.obtener_pizza()
pizza_pepperoni.mostrar_pizza()

pizza_vegetariana_builder = PizzaVegetarianaBuilder()
pizzeria.construir_pizza(pizza_vegetariana_builder)
pizza_vegetariana = pizzeria.obtener_pizza()
pizza_vegetariana.mostrar_pizza()

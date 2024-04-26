from __future__ import annotations
from abc import ABC, abstractmethod


# Componente: AbstractFactory (Fábrica Abstracta)
class AbstractFactory(ABC):
    """
    La interfaz Abstract Factory declara un conjunto de métodos que devuelven
    diferentes productos abstractos. Estos productos se denominan familia y
    están relacionados por un tema o concepto de alto nivel. Los productos de
    una familia suelen poder colaborar entre sí. Una familia de productos puede
    tener varias variantes, pero los productos de una variante son incompatibles
    con los productos de otra..
    """
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


# Fábrica Concreta 1 (ConcreteFactory1)
class ConcreteFactory1(AbstractFactory):
    """
    Las Fábricas Concretas producen una familia de productos que pertenecen a
    una sola variante. La fábrica garantiza que los productos resultantes sean
    compatibles. Ten en cuenta que las firmas de los métodos de la Fábrica
    Concreta devuelven un producto abstracto, mientras que dentro del método se
    instancia un producto concreto.
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


# Fábrica Concreta 2 (ConcreteFactory2)
class ConcreteFactory2(AbstractFactory):
    """
    Cada Fábrica Concreta tiene una variante de producto correspondiente.
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


# Producto Abstracto A (AbstractProductA)
class AbstractProductA(ABC):
    """
    Cada producto distinto de una familia de productos debe tener una interfaz
    base. Todas las variantes del producto deben implementar esta interfaz.
    """

    @abstractmethod
    def useful_function_a(self) -> str:
        pass


"""
Los productos concretos son creados por las correspondientes fábricas concretas.
"""


# Producto Concreto A1 (ConcreteProductA1)
class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "El resultado del producto A1."


# Producto Concreto A2 (ConcreteProductA2)
class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self) -> str:
        return "El resultado del producto A2."


# Producto Abstracto B (AbstractProductB)
class AbstractProductB(ABC):
    """
    Aquí está la interfaz base de otro producto. Todos los productos pueden
    interactuar entre sí, pero la interacción adecuada solo es posible entre
    productos de la misma variante concreta.

    """
    @abstractmethod
    def useful_function_b(self) -> None:
        """
        El Producto B es capaz de hacer lo suyo...
        """
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA) -> None:
        """
        ...pero también puede colaborar con el ProductoA.

        Abstract Factory se asegura de que todos los productos que
        crea sean de la misma variante y, por lo tanto, compatibles.
        """
        pass


"""
Los productos concretos son creados por las correspondientes fábricas concretas.
"""


# Producto Concreto B1 (ConcreteProductB1)
class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self) -> str:
        return "El resultado del producto B1."

    """
    La variante, Producto B1, solo puede funcionar correctamente 
    con la variante, Producto A1. Sin embargo, acepta cualquier 
    instancia de AbstractProductA como argumento.
    """

    def another_useful_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_function_a()
        return f"El resultado del B1 colaborando con el ({result})"


# Producto Concreto B2 (ConcreteProductB2)
class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self) -> str:
        return "El resultado del producto B2."

    def another_useful_function_b(self, collaborator: AbstractProductA):
        """
        La variante, Producto B2, solo puede funcionar correctamente con
        la variante, Producto A2. Sin embargo, acepta cualquier instancia
        de AbstractProductA como argumento.
        """
        result = collaborator.useful_function_a()
        return f"El resultado del B2 colaborando con el ({result})"


# Código del cliente o interface del cleinte (Clien_Code)
def client_code(factory: AbstractFactory) -> None:
    """
    El código del cliente trabaja solo con fábricas y productos del tipo abstracto:
    AbstractFactory y AbstractProduct. Esto permite pasar cualquier subclase de
    fábrica o producto al código del cliente sin romperlo.
    """
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.useful_function_b()}")
    print(f"{product_b.another_useful_function_b(product_a)}", end="")


if __name__ == "__main__":
    """
    El código del cliente puede funcionar con cualquier 
    clase de fábrica concreta.
    """
    print("Cliente: Probando el código del cliente con la primera fábrica concreta:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Cliente: Probando el mismo código del cliente con la segunda fábrica concreta:")
    client_code(ConcreteFactory2())

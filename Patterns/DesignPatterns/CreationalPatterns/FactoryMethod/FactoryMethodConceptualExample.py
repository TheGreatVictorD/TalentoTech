from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    """
    La clase Creator declara el método de fábrica que se supone que debe
    devolver un objeto de una clase Producto. Las subclases del Creador
    suelen proporcionar la implementación de este método.
    """

    @abstractmethod
    def factory_method(self):
        """
        Tenga en cuenta que el Creador también puede proporcionar alguna
        implementación predeterminada del método de fábrica.
        """
        pass

    def some_operation(self) -> str:
        """
        También tenga en cuenta que, a pesar de su nombre, la responsabilidad
        principal del Creador no es crear productos. Por lo general, contiene
        alguna lógica empresarial central que se basa en objetos Producto,
        devueltos por el método de fábrica.
        Las subclases pueden cambiar indirectamente esa lógica empresarial
        anulando el método de fábrica y devolviendo un tipo diferente de producto.
        """

        # Call the factory method to create a Product object.
        product = self.factory_method()

        # Now, use the product.
        result = f"Creador: El mismo código del creador acaba de trabajar con {product.operation()}"

        return result


"""
Los creadores Concretos anulan el método de fábrica para 
cambiar el tipo de producto resultante.
"""


class ConcreteCreator1(Creator):
    """
    Tenga en cuenta que la firma del método todavía utiliza el tipo
    de producto abstracto, aunque el producto concreto en realidad
    se devuelve desde el método. De esta manera, el Creador puede
    permanecer independiente de clases de productos concretas.
    """

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):
    """
    La interfaz del Producto declara las operaciones que todos
    los productos concretos deben implementar..
    """

    @abstractmethod
    def operation(self) -> str:
        pass


"""
Los productos concretos proporcionan varias implementaciones de la interfaz del Producto.
"""


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Resultado del ProductoConcreto1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Resultado del ProductoConcreto2}"


def client_code(creator: Creator) -> None:
    """
    El código del cliente funciona con una instancia de un creador concreto,
    aunque a través de su interfaz base. Mientras el cliente siga trabajando
    con el creador a través de la interfaz base, puede pasarle cualquier
    subclase del creador..
    """

    print(f"Cliente: No conozco la clase del creador, pero aún así funciona.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Lanzada con ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print("App: Lanzado con ConcreteCreator2.")
    client_code(ConcreteCreator2())

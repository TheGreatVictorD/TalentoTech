from __future__ import annotations
from abc import ABC, abstractmethod


# Clase abstracta Creator que representa la Abstract Factory
class Creator(ABC):
    """
    La clase Creator declara el método de fábrica que se supone que devuelve un
    objeto de una clase Product. Las subclases de Creator suelen proporcionar la
    implementación de este método.
    """

    @abstractmethod
    def factory_method(self):
        """
        Tenga en cuenta que el Creator también puede proporcionar alguna
        implementación predeterminada del método de fábrica.
        """
        pass

    def some_operation(self) -> str:
        """
        También tenga en cuenta que, a pesar de su nombre, la responsabilidad
        principal del Creator no es crear productos. Por lo general, contiene
        alguna lógica empresarial central que depende de objetos Product, devueltos
        por el método de fábrica. Las subclases pueden cambiar indirectamente
        esa lógica empresarial al anular el método de fábrica y devolver un
        tipo diferente de producto desde él.
        """

        # Llama al método de fábrica para crear un objeto Product.
        product = self.factory_method()

        # Ahora, usa el producto.
        result = f"Creator: El mismo código del creador acaba de funcionar con {product.operation()}"

        return result


# Los Concrete Creators anulan el método de fábrica para cambiar el tipo de producto resultante.

# Clase ConcreteCreator1 que implementa la Concrete Factory
class ConcreteCreator1(Creator):
    """
    Tenga en cuenta que la firma del método aún usa el tipo de producto abstracto,
    aunque el producto concreto se devuelve realmente del método. De esta manera, el
    Creator puede permanecer independiente de las clases de producto concretas.
    """

    def factory_method(self) -> Product:
        return ConcreteProduct1()


# Clase ConcreteCreator2 que implementa la Concrete Factory
class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


# Clase abstracta Product que representa la interfaz de los productos
class Product(ABC):
    """
    La interfaz Product declara las operaciones que todos los productos concretos
    deben implementar.
    """

    @abstractmethod
    def operation(self) -> str:
        pass


# Los Concrete Products proporcionan diversas implementaciones de la interfaz Product.

# Clase ConcreteProduct1 que implementa un producto concreto
class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Resultado del ConcreteProduct1}"


# Clase ConcreteProduct2 que implementa un producto concreto
class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Resultado del ConcreteProduct2}"


# Función client_code que representa el código del cliente
def client_code(creator: Creator) -> None:
    """
    El código de cliente funciona solo con fábricas y productos de
    tipo abstracto: AbstractFactory y AbstractProduct. Esto le permite
    pasar cualquier subclase de fábrica o producto al código de cliente
    sin romperlo.
    """

    print(f"Cliente: No conozco la clase del creador, pero aún funciona.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Iniciada con ConcreteCreator1.")
    client_code(ConcreteCreator1())
    print("\n")

    print(": Iniciada con ConcreteCreator2.")
    client_code(ConcreteCreator2())

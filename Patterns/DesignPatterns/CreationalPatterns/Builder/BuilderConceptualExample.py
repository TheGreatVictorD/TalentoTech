from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    """
    La interfaz Builder especifica métodos para crear las
    diferentes partes de los objetos del Producto.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class ConcreteBuilder1(Builder):
    """
    Las clases de Concrete Builder siguen la interfaz de Builder y
    proporcionan implementaciones específicas de los pasos de construcción.
    Su programa puede tener varias variaciones de Builders, implementadas
    de manera diferente.
    """

    def __init__(self) -> None:
        """
        Una instancia de constructor nueva debe contener un objeto de
        producto en blanco, que se utiliza en el ensamblaje posterior.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        """
        Se supone que Concrete Builders deben proporcionar sus propios métodos
        para obtener resultados. Esto se debe a que varios tipos de constructores
        pueden crear productos completamente diferentes que no siguen la misma interfaz.
        Por lo tanto, dichos métodos no se pueden declarar en la interfaz básica del
        Builder (al menos en un lenguaje de programación de tipo estático).

        Por lo general, después de devolver el resultado final al cliente, se espera que
        una instancia de construcción esté lista para comenzar a producir otro producto.
        Por eso es una práctica habitual llamar al método reset al final del cuerpo del
        método `getProduct`. Sin embargo, este comportamiento no es obligatorio y puede
        hacer que sus constructores esperen una llamada de reinicio explícita desde el
        código del cliente antes de deshacerse del resultado anterior.
        """
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartA1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")


class Product1:
    """
    Tiene sentido utilizar el patrón Builder sólo cuando sus productos son bastante
    complejos y requieren una configuración extensa.

    A diferencia de otros patrones creacionales, diferentes constructores concretos
    pueden producir productos no relacionados. En otras palabras, es posible que los
    resultados de varios constructores no siempre sigan la misma interfaz.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:
    """
    El Director sólo es responsable de ejecutar los pasos de construcción en una
    secuencia particular. Resulta útil a la hora de producir productos según un
    pedido o configuración específicos. Estrictamente hablando, la clase Director
    es opcional, ya que el cliente puede controlar a los constructores directamente.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
       El Director trabaja con cualquier instancia de constructor
       que le pase el código del cliente. De esta forma, el código
       del cliente puede alterar el tipo final del producto recién
       ensamblado.
        """
        self._builder = builder

    """
    El director puede construir varias variaciones de productos siguiendo
    los mismos pasos de construcción.
    """

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == "__main__":
    """
    El código del cliente crea un objeto constructor, lo pasa al 
    director y luego inicia el proceso de construcción. El resultado 
    final se recupera del objeto constructor.
    """

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Producto básico estándar: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Producto estándar con todas las funciones: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Producto personalizado: ")
    builder.produce_part_a()
    builder.produce_part_b()
    builder.product.list_parts()

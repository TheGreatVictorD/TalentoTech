from __future__ import annotations
from abc import ABC, abstractmethod


# Creator abstracto
class FabricaGalletas(ABC):
    @abstractmethod
    def crear_galleta(self) -> Galleta:
        pass

    def obtener_galleta(self) -> str:
        galleta = self.crear_galleta()
        return f"Obteniendo una {galleta.forma()}"


# Creadores concretos
class FabricaGalletaDePerro(FabricaGalletas):
    def crear_galleta(self) -> Galleta:
        return GalletaDePerro()


class FabricaGalletaDeGato(FabricaGalletas):
    def crear_galleta(self) -> Galleta:
        return GalletaDeGato()


class FabricaGalletaDeJirafa(FabricaGalletas):
    def crear_galleta(self) -> Galleta:
        return GalletaDeJirafa()


# Producto abstracto
class Galleta(ABC):
    @abstractmethod
    def forma(self) -> str:
        pass


# Productos concretos
class GalletaDePerro(Galleta):
    def forma(self) -> str:
        return "Galleta con forma de perro"


class GalletaDeGato(Galleta):
    def forma(self) -> str:
        return "Galleta con forma de gato"


class GalletaDeJirafa(Galleta):
    def forma(self) -> str:
        return "Galleta con forma de jirafa"


# Cliente
def cliente(creator: FabricaGalletas) -> None:
    print(f"Cliente: Interacción con la fábrica de galletas.")
    print(creator.obtener_galleta())


if __name__ == "__main__":
    print("App: Lanzada con FabricaGalletaDePerro.")
    cliente(FabricaGalletaDePerro())
    print("\n")

    print("App: Lanzada con FabricaGalletaDeGato.")
    cliente(FabricaGalletaDeGato())
    print("\n")

    print("App: Lanzada con FabricaGalletaDeJirafa.")
    cliente(FabricaGalletaDeJirafa())


"""
Relaciones entre las clases:

- Herencia: Las clases GalletaDePerro, GalletaDeGato y GalletaDeJirafa heredan de la clase abstracta Galleta. 
Esto se representa en el diagrama UML con las flechas que apuntan de GalletaDePerro, GalletaDeGato y GalletaDeJirafa a 
Galleta con un triángulo en la punta (<|--).

- Herencia: Las clases FabricaGalletaDePerro, FabricaGalletaDeGato y FabricaGalletaDeJirafa heredan de la clase 
abstracta FabricaGalletas. Esto se representa en el diagrama UML con las flechas que apuntan de FabricaGalletaDePerro, 
FabricaGalletaDeGato y FabricaGalletaDeJirafa a FabricaGalletas con un triángulo en la punta (<|--).

- Dependencia: La clase FabricaGalletas tiene una dependencia hacia la clase Galleta. Esto se debe a que FabricaGalletas
utiliza a Galleta en su método crear_galleta(). En el diagrama UML, esto se representa con una flecha punteada que 
apunta de FabricaGalletas a Galleta (..>).

Por lo tanto, las relaciones entre las clases en el código son de herencia y dependencia.
"""
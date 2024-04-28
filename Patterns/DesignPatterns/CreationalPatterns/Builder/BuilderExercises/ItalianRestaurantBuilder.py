from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


# Interfaz Builder
class OrderBuilder(ABC):
    @property
    @abstractmethod
    def order(self) -> None:
        pass

    @abstractmethod
    def add_green_sorrentinos(self) -> None:
        pass

    @abstractmethod
    def add_cappelletti(self) -> None:
        pass

    @abstractmethod
    def add_ravioli_di_pietro(self) -> None:
        pass

    @abstractmethod
    def add_rigatoni_with_tomato_and_bacon(self) -> None:
        pass

    @abstractmethod
    def add_traditional_meat_cannelloni_with_bechamel(self) -> None:
        pass

    @abstractmethod
    def add_red_wine(self) -> None:
        pass

    @abstractmethod
    def add_craft_beer(self) -> None:
        pass

    @abstractmethod
    def add_white_wine(self) -> None:
        pass

    @abstractmethod
    def add_wheat_beer(self) -> None:
        pass

    @abstractmethod
    def add_dry_white_wine(self) -> None:
        pass

    @abstractmethod
    def add_lager_beer(self) -> None:
        pass


# Constructores Concretos
class CustomOrderBuilder(OrderBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._order = MainOrder()

    @property
    def order(self) -> MainOrder:
        order = self._order
        self.reset()
        return order

    def add_green_sorrentinos(self) -> None:
        self._order.add('Sorrentinos Verdes: Pasta verde rellena de ricota, mozzarella y albahaca, '
                        'gratinados con Pomodoro Fresco y bechamel')

    def add_cappelletti(self) -> None:
        self._order.add('Cappelletti: Pasta rellena de lomo, mortadela italiana y jamón crudo, '
                        'con salsa de tomates frescos.')

    def add_ravioli_di_pietro(self) -> None:
        self._order.add('Ravioli Di Pietro: Ravioles de masa de rúcula fresca y rellenos de lomo y hongos, '
                        'en salsa de tomates frescos.')

    def add_rigatoni_with_tomato_and_bacon(self) -> None:
        self._order.add('Rigatoni con Tomate y Beicon: Rigatoni con tomate y beicon, '
                        'aderezado con albahaca y parmesano.')

    def add_traditional_meat_cannelloni_with_bechamel(self) -> None:
        self._order.add('Canelones de Carne Tradicionales con Bechamel: Canelones rellenos de carne, '
                        'cubiertos con salsa bechamel.')

    def add_red_wine(self) -> None:
        self._order.add('Vino tinto: Un vino tinto ligero o de cuerpo medio como un Chianti o un Merlot pueden resaltar'
                        ' los sabores de la salsa de tomate sin opacarlos.')

    def add_craft_beer(self) -> None:
        self._order.add('Cerveza artesanal: Una cerveza estilo IPA o una cerveza ámbar pueden equilibrar los sabores '
                        'ácidos de la salsa de tomate y realzar los sabores de la pasta')

    def add_white_wine(self) -> None:
        self._order.add('Vino blanco: Un vino blanco seco como un Chardonnay o un Sauvignon Blanc pueden complementar '
                        'los sabores cremosos de la salsa sin abrumarlos.')

    def add_wheat_beer(self) -> None:
        self._order.add('Cerveza de trigo: Una cerveza de trigo suave y refrescante puede contrarrestar la cremosidad '
                        'de la salsa y ofrecer un equilibrio a los sabores')

    def add_dry_white_wine(self) -> None:
        self._order.add('Vino blanco seco: Un vino blanco seco y afrutado como un Riesling o un Albariño puede realzar '
                        'los sabores del marisco sin dominarlos.')

    def add_lager_beer(self) -> None:
        self._order.add('Cerveza tipo Lager: Una cerveza tipo Lager ligera y refrescante puede complementar los sabores'
                        ' delicados de los mariscos sin competir con ellos')


# Producto
class MainOrder:
    def __init__(self) -> None:
        self.items = []

    def add(self, item: Any) -> None:
        self.items.append(item)

    def list_items(self) -> None:
        print(f"Order plates:\n{'\n'.join('\t-' + item for item in self.items)}")


# Director
class ItalianRestaurant:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> OrderBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: OrderBuilder) -> None:
        self._builder = builder

    def build_white_wine_green_custom_order(self) -> None:
        self.builder.add_green_sorrentinos()
        self.builder.add_white_wine()

    def build_classic_cappeletti_custom_order(self) -> None:
        self.builder.add_cappelletti()
        self.builder.add_red_wine()

    def build_ravioli_rosso_custom_order(self) -> None:
        self.builder.add_ravioli_di_pietro()
        self.builder.add_dry_white_wine()

    def build_refreshing_rigatoni(self) -> None:
        self.builder.add_rigatoni_with_tomato_and_bacon()
        self.builder.add_craft_beer()

    def build_creamy_cannelloni(self) -> None:
        self.builder.add_traditional_meat_cannelloni_with_bechamel()
        self.builder.add_lager_beer()


if __name__ == "__main__":
    director = ItalianRestaurant()
    builder = CustomOrderBuilder()
    director.builder = builder

    print("Standard order: Verde Vino Blanco")
    director.build_white_wine_green_custom_order()
    builder.order.list_items()

    print("\n")

    print("Standard order: Cappeletti Clásico")
    director.build_classic_cappeletti_custom_order()
    builder.order.list_items()

    print("\n")

    print("Standard order: Ravioli Rosso")
    director.build_ravioli_rosso_custom_order()
    builder.order.list_items()

    print("\n")

    print("Standard order: Rigatoni Refrescante")
    director.build_refreshing_rigatoni()
    builder.order.list_items()

    print("\n")

    print("Standard order: Canelones Cremosos")
    director.build_creamy_cannelloni()
    builder.order.list_items()

from abc import ABC, abstractmethod


# Producto: Computadora
class Computer:
    def __init__(self):
        self.specs = []

    def add_component(self, component):
        self.specs.append(component)

    def show_specs(self):
        print("Computer specifications:")
        for spec in self.specs:
            print(f"- {spec}")


# Builder: Interfaz para construir computadoras
class ComputerBuilder(ABC):
    @abstractmethod
    def build_graphics_card(self):
        pass

    @abstractmethod
    def build_storage(self):
        pass

    @abstractmethod
    def build_display(self):
        pass

    @abstractmethod
    def get_computer(self):
        pass


# Concrete Builders: Implementaciones específicas de los pasos de construcción
class BasicComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def build_graphics_card(self):
        self.computer.add_component("Basic Graphics Card")

    def build_storage(self):
        self.computer.add_component("HDD")

    def build_display(self):
        self.computer.add_component("Standard Display")

    def get_computer(self):
        return self.computer


class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def build_graphics_card(self):
        self.computer.add_component("Gaming Graphics Card")

    def build_storage(self):
        self.computer.add_component("SSD")

    def build_display(self):
        self.computer.add_component("High-Resolution Display")

    def get_computer(self):
        return self.computer


# Director: Coordina los pasos de construcción
class ComputerEngineer:
    def __init__(self, builder):
        self.builder = builder

    def construct_computer(self):
        self.builder.build_graphics_card()
        self.builder.build_storage()
        self.builder.build_display()

    def get_computer(self):
        return self.builder.get_computer()


# Uso del patrón Builder
if __name__ == "__main__":
    # Crear un ingeniero de computadoras con un builder específico
    basic_builder = BasicComputerBuilder()
    engineer = ComputerEngineer(basic_builder)

    # Construir una computadora básica
    engineer.construct_computer()
    computer = engineer.get_computer()
    computer.show_specs()

    print("\n")

    # Crear un ingeniero de computadoras con otro builder
    gaming_builder = GamingComputerBuilder()
    engineer = ComputerEngineer(gaming_builder)

    # Construir una computadora para juegos
    engineer.construct_computer()
    computer = engineer.get_computer()
    computer.show_specs()

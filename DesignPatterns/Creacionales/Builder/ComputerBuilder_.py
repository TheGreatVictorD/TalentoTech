from abc import ABC, abstractmethod


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

    def show_specs(self, computer):
        print("Computer specifications:")
        for key, value in computer.items():
            print(f"- {key}: {value}")


# Constructores Concretos: Implementaciones específicas del Builder
class BasicComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = {}

    def build_graphics_card(self):
        self.computer['graphics_card'] = "Basic Graphics Card"

    def build_storage(self):
        self.computer['storage'] = "HDD"

    def build_display(self):
        self.computer['display'] = "Standard Display"

    def get_computer(self):
        return self.computer


class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = {}

    def build_graphics_card(self):
        self.computer['graphics_card'] = "Gaming Graphics Card"

    def build_storage(self):
        self.computer['storage'] = "SSD"

    def build_display(self):
        self.computer['display'] = "High-Resolution Display"

    def get_computer(self):
        return self.computer


# Director: Coordina los pasos de construcción
class ComputerEngineer:
    def __init__(self, builder: ComputerBuilder):
        self.builder = builder

    def construct_computer(self):
        self.builder.build_graphics_card()
        self.builder.build_storage()
        self.builder.build_display()

    def get_computer(self):
        return self.builder.get_computer()

    def show_computer_specs(self):
        computer = self.builder.get_computer()
        self.builder.show_specs(computer)


# Uso del patrón Builder
if __name__ == "__main__":
    # Crear un ingeniero de computadoras con un builder específico
    basic_builder = BasicComputerBuilder()
    engineer = ComputerEngineer(basic_builder)

    # Construir una computadora básica
    engineer.construct_computer()
    engineer.show_computer_specs()

    print("\n")

    # Crear un ingeniero de computadoras con otro builder
    gaming_builder = GamingComputerBuilder()
    engineer = ComputerEngineer(gaming_builder)

    # Construir una computadora para juegos
    engineer.construct_computer()
    engineer.show_computer_specs()

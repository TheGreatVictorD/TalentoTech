from abc import ABC, abstractmethod
import platform


# Interfaz fábrica abstracta
class GUIFactory(ABC):
    """
    GUI significa "Interfaz Gráfica de Usuario" (Graphical User Interface en inglés)
    """
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


# Fábrica concreta para Windows
class WinFactory(GUIFactory):
    def create_button(self):
        return WinButton()

    def create_checkbox(self):
        return WinCheckbox()


# Fábrica concreta para macOS
class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


# Interfaz base para el producto Button
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass


# Producto concreto para botón Windows
class WinButton(Button):
    def paint(self):
        print("Representa un botón en estilo Windows.")


# Producto concreto para botón macOS
class MacButton(Button):
    def paint(self):
        print("Representa un botón en estilo macOS.")


# Interfaz base para el producto Checkbox
class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass


# Producto concreto para casilla de verificación Windows
class WinCheckbox(Checkbox):
    def paint(self):
        print("Representa una casilla en estilo Windows.")


# Producto concreto para casilla de verificación macOS
class MacCheckbox(Checkbox):
    def paint(self):
        print("Representa una casilla en estilo macOS.")


# Código cliente
class Application:
    def __init__(self, factory: GUIFactory):
        self.factory = factory
        self.button = None
        self.checkbox = None

    def create_ui(self):
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()

    def paint(self):
        if self.button:
            self.button.paint()
        if self.checkbox:
            self.checkbox.paint()


# Configurador de la aplicación
class ApplicationConfigurator:
    @staticmethod
    def main():
        config = read_application_config_file()
        if config["OS"] == "Windows":  # Acceder al atributo OS del diccionario
            factory = WinFactory()
        elif config["OS"] == "Mac":  # Acceder al atributo OS del diccionario
            factory = MacFactory()
        else:
            raise Exception("Error! Unknown operating system.")

        app = Application(factory)
        app.create_ui()
        app.paint()


def read_application_config_file():
    # Esta función debería leer la configuración del archivo y devolver un objeto de configuración
    os = platform.system()
    # Aquí se asume que `config` tiene una propiedad `OS` que indica el sistema operativo
    config = {"OS": os}  # Ejemplo de configuración
    return config


# Ejecutar la aplicación
if __name__ == "__main__":
    ApplicationConfigurator.main()

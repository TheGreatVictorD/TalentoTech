from abc import ABC, abstractmethod


# Clase Producto
class Automovil:
    def __init__(self):
        self.tipo = ""
        self.motor = ""
        self.transmision = ""
        self.interiores = ""

    def agregar_tipo(self, tipo):
        self.tipo = tipo

    def agregar_motor(self, motor):
        self.motor = motor

    def agregar_transmision(self, transmision):
        self.transmision = transmision

    def agregar_interiores(self, interiores):
        self.interiores = interiores

    def mostrar_automovil(self):
        print(f"Tipo de automóvil: {self.tipo}")
        print(f"Motor: {self.motor}")
        print(f"Transmisión: {self.transmision}")
        print(f"Interiores: {self.interiores}")
        print("¡Disfruta tu automóvil!")


# Interfaz Builder
class AutomovilBuilder(ABC):
    def __init__(self):
        self.automovil = Automovil()

    @abstractmethod
    def agregar_tipo(self):
        pass

    @abstractmethod
    def agregar_motor(self):
        pass

    @abstractmethod
    def agregar_transmision(self):
        pass

    @abstractmethod
    def agregar_interiores(self):
        pass

    def obtener_automovil(self):
        return self.automovil


# Constructores Concretos
class AutoFamiliarBuilder(AutomovilBuilder):
    def agregar_tipo(self):
        self.automovil.agregar_tipo("Auto Familiar")

    def agregar_motor(self):
        self.automovil.agregar_motor("Motor estándar de 4 cilindros")

    def agregar_transmision(self):
        self.automovil.agregar_transmision("Caja de velocidades manual")

    def agregar_interiores(self):
        self.automovil.agregar_interiores("Interiores en materiales sintéticos")


class AutoDeportivoBuilder(AutomovilBuilder):
    def agregar_tipo(self):
        self.automovil.agregar_tipo("Auto Deportivo")

    def agregar_motor(self):
        self.automovil.agregar_motor("Motor de alto rendimiento V8")

    def agregar_transmision(self):
        self.automovil.agregar_transmision("Caja de velocidades automática")

    def agregar_interiores(self):
        self.automovil.agregar_interiores("Interiores en materiales premium como cuero")


class PickupBuilder(AutomovilBuilder):
    def agregar_tipo(self):
        self.automovil.agregar_tipo("Pickup")

    def agregar_motor(self):
        self.automovil.agregar_motor("Motor de alto torque V6")

    def agregar_transmision(self):
        self.automovil.agregar_transmision("Caja de velocidades automática")

    def agregar_interiores(self):
        self.automovil.agregar_interiores("Interiores en materiales premium como cuero")


# Director
class FabricaAutomoviles:
    def __init__(self):
        self.builder = None

    def construir_automovil(self, builder):
        self.builder = builder
        self.builder.agregar_tipo()
        self.builder.agregar_motor()
        self.builder.agregar_transmision()
        self.builder.agregar_interiores()

    def obtener_automovil(self):
        return self.builder.obtener_automovil()


# Uso del Builder
fabrica = FabricaAutomoviles()

auto_familiar_builder = AutoFamiliarBuilder()
fabrica.construir_automovil(auto_familiar_builder)
auto_familiar = fabrica.obtener_automovil()
auto_familiar.mostrar_automovil()

auto_deportivo_builder = AutoDeportivoBuilder()
fabrica.construir_automovil(auto_deportivo_builder)
auto_deportivo = fabrica.obtener_automovil()
auto_deportivo.mostrar_automovil()

pickup_builder = PickupBuilder()
fabrica.construir_automovil(pickup_builder)
pickup = fabrica.obtener_automovil()
pickup.mostrar_automovil()

from abc import ABC, abstractmethod


# Interfaz para el motor
class Engine(ABC):
    @abstractmethod
    def start(self):
        pass


# Interfaz para la transmisión
class Transmission(ABC):
    @abstractmethod
    def shift_gear(self):
        pass


# Interfaz para los neumáticos
class Tire(ABC):
    @abstractmethod
    def pressure(self):
        pass


# Fábrica abstracta para crear componentes del vehículo
class VehicleFactory(ABC):
    @abstractmethod
    def create_engine(self) -> Engine:
        pass

    @abstractmethod
    def create_transmission(self) -> Transmission:
        pass

    @abstractmethod
    def create_tire(self) -> Tire:
        pass


# Fábrica concreta para vehículos en Estados Unidos
class USVehicleFactory(VehicleFactory):
    def create_engine(self) -> Engine:
        return USEngine()

    def create_transmission(self) -> Transmission:
        return USTransmission()

    def create_tire(self) -> Tire:
        return USTire()


# Fábrica concreta para vehículos en Europa
class EUVehicleFactory(VehicleFactory):
    def create_engine(self) -> Engine:
        return EUEngine()

    def create_transmission(self) -> Transmission:
        return EUTransmission()

    def create_tire(self) -> Tire:
        return EUTire()


# Clases concretas para componentes de vehículos en Estados Unidos
class USEngine(Engine):
    def start(self):
        print("Motor iniciado (Estados Unidos)")


class USTransmission(Transmission):
    def shift_gear(self):
        print("Cambio de marcha realizado (Estados Unidos)")


class USTire(Tire):
    def pressure(self):
        print("Presión de neumáticos verificada (Estados Unidos)")


# Clases concretas para componentes de vehículos en Europa
class EUEngine(Engine):
    def start(self):
        print("Motor iniciado (Europa)")


class EUTransmission(Transmission):
    def shift_gear(self):
        print("Cambio de marcha realizado (Europa)")


class EUTire(Tire):
    def pressure(self):
        print("Presión de neumáticos verificada (Europa)")


# Cliente
class Client:
    def __init__(self, factory: VehicleFactory):
        self.factory = factory

    def assemble_vehicle(self):
        engine = self.factory.create_engine()
        transmission = self.factory.create_transmission()
        tire = self.factory.create_tire()

        engine.start()
        transmission.shift_gear()
        tire.pressure()


# Ejemplo de uso
if __name__ == "__main__":
    us_factory = USVehicleFactory()
    client_us = Client(us_factory)
    client_us.assemble_vehicle()

    print()  # Salto de línea

    eu_factory = EUVehicleFactory()
    client_eu = Client(eu_factory)
    client_eu.assemble_vehicle()

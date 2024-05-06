# Producto Abstracto
class Vehiculo:
    def mostrar_info(self):
        raise NotImplementedError("Debes implementar este método en la clase concreta.")


# Productos Concretos
class Automovil(Vehiculo):
    def mostrar_info(self):
        return "Este es un automóvil."


class Motocicleta(Vehiculo):
    def mostrar_info(self):
        return "Esta es una motocicleta."


# Fábrica Abstracta
class FabricaVehiculos:
    def crear_vehiculo(self):
        raise NotImplementedError("Debes implementar este método en la clase concreta.")


# Fábricas Concretas
class FabricaAutomoviles(FabricaVehiculos):
    def crear_vehiculo(self):
        return Automovil()


class FabricaMotocicletas(FabricaVehiculos):
    def crear_vehiculo(self):
        return Motocicleta()


# Cliente
class Cliente:
    def __init__(self, fabrica):
        self.fabrica = fabrica

    def mostrar_vehiculo(self):
        vehiculo = self.fabrica.crear_vehiculo()
        return vehiculo.mostrar_info()


# Uso del patrón
fabrica_automoviles = FabricaAutomoviles()
cliente_automoviles = Cliente(fabrica_automoviles)
print(cliente_automoviles.mostrar_vehiculo())  # Salida: "Este es un automóvil."

fabrica_motocicletas = FabricaMotocicletas()
cliente_motocicletas = Cliente(fabrica_motocicletas)
print(cliente_motocicletas.mostrar_vehiculo())  # Salida: "Esta es una motocicleta."

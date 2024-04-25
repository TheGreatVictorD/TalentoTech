from abc import ABC, abstractmethod


# Clase Producto
class Computadora:
    def __init__(self):
        self.tipo = ""
        self.procesador = ""
        self.memoria_ram = ""
        self.almacenamiento = ""
        self.tarjeta_video = ""

    def agregar_tipo(self, tipo):
        self.tipo = tipo

    def agregar_procesador(self, procesador):
        self.procesador = procesador

    def agregar_memoria_ram(self, memoria_ram):
        self.memoria_ram = memoria_ram

    def agregar_almacenamiento(self, almacenamiento):
        self.almacenamiento = almacenamiento

    def agregar_tarjeta_video(self, tarjeta_video):
        self.tarjeta_video = tarjeta_video

    def mostrar_computadora(self):
        print(f"Tipo de computadora: {self.tipo}")
        print(f"    -Procesador: {self.procesador}")
        print(f"    -Memoria RAM: {self.memoria_ram}")
        print(f"    -Almacenamiento: {self.almacenamiento}")
        print(f"    -Tarjeta de video: {self.tarjeta_video}")
        print("    ¡Disfruta tu computadora\n")


# Interfaz Builder
class ComputadoraBuilder(ABC):
    def __init__(self):
        self.computadora = Computadora()

    @abstractmethod
    def agregar_tipo(self):
        pass

    @abstractmethod
    def agregar_procesador(self):
        pass

    @abstractmethod
    def agregar_memoria_ram(self):
        pass

    @abstractmethod
    def agregar_almacenamiento(self):
        pass

    @abstractmethod
    def agregar_tarjeta_video(self):
        pass

    def obtener_computadora(self):
        return self.computadora


# Constructores Concretos
class ComputadoraEscritorioBuilder(ComputadoraBuilder):
    def agregar_tipo(self):
        self.computadora.agregar_tipo("Computadora de Escritorio")

    def agregar_procesador(self):
        self.computadora.agregar_procesador("Intel Core i5")

    def agregar_memoria_ram(self):
        self.computadora.agregar_memoria_ram("8GB DDR4")

    def agregar_almacenamiento(self):
        self.computadora.agregar_almacenamiento("1TB HDD")

    def agregar_tarjeta_video(self):
        self.computadora.agregar_tarjeta_video("Integrada")


class ComputadoraPortatilBuilder(ComputadoraBuilder):
    def agregar_tipo(self):
        self.computadora.agregar_tipo("Computadora Portátil")

    def agregar_procesador(self):
        self.computadora.agregar_procesador("AMD Ryzen 7")

    def agregar_memoria_ram(self):
        self.computadora.agregar_memoria_ram("16GB DDR4")

    def agregar_almacenamiento(self):
        self.computadora.agregar_almacenamiento("512GB SSD")

    def agregar_tarjeta_video(self):
        self.computadora.agregar_tarjeta_video("NVIDIA GeForce GTX 1650")


class EstacionTrabajoBuilder(ComputadoraBuilder):
    def agregar_tipo(self):
        self.computadora.agregar_tipo("Estación de Trabajo")

    def agregar_procesador(self):
        self.computadora.agregar_procesador("Intel Xeon")

    def agregar_memoria_ram(self):
        self.computadora.agregar_memoria_ram("32GB ECC DDR4")

    def agregar_almacenamiento(self):
        self.computadora.agregar_almacenamiento("2TB NVMe SSD")

    def agregar_tarjeta_video(self):
        self.computadora.agregar_tarjeta_video("NVIDIA Quadro RTX 4000")


# Director
class FabricaComputadoras:
    def __init__(self):
        self.builder = None

    def construir_computadora(self, builder):
        self.builder = builder
        self.builder.agregar_tipo()
        self.builder.agregar_procesador()
        self.builder.agregar_memoria_ram()
        self.builder.agregar_almacenamiento()
        self.builder.agregar_tarjeta_video()

    def obtener_computadora(self):
        return self.builder.obtener_computadora()


# Uso del Builder
fabrica = FabricaComputadoras()

computadora_escritorio_builder = ComputadoraEscritorioBuilder()
fabrica.construir_computadora(computadora_escritorio_builder)
computadora_escritorio = fabrica.obtener_computadora()
computadora_escritorio.mostrar_computadora()


computadora_portatil_builder = ComputadoraPortatilBuilder()
fabrica.construir_computadora(computadora_portatil_builder)
computadora_portatil = fabrica.obtener_computadora()
computadora_portatil.mostrar_computadora()


estacion_trabajo_builder = EstacionTrabajoBuilder()
fabrica.construir_computadora(estacion_trabajo_builder)
estacion_trabajo = fabrica.obtener_computadora()
estacion_trabajo.mostrar_computadora()

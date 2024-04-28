# Clase Producto
class Libro:
    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio


# Clase Pedido
class Pedido:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_pedido(self):
        total = sum(libro.precio for libro in self.libros)
        print("Libros en el pedido:")
        for libro in self.libros:
            print(f"- {libro.titulo} de {libro.autor}")
        print(f"Total a pagar: ${total:.2f}")


# Builder para construir pedidos
class PedidoBuilder:
    def __init__(self):
        self.pedido = Pedido()

    def agregar_libro(self, titulo, autor, precio):
        libro = Libro(titulo, autor, precio)
        self.pedido.agregar_libro(libro)

    def obtener_pedido(self):
        return self.pedido


# Director que maneja la construcción del pedido
class Tienda:
    def __init__(self):
        self.builder = None

    def construir_pedido(self, builder):
        self.builder = builder
        self.builder.agregar_libro("El señor de los anillos", "J.R.R. Tolkien", 25.99)
        self.builder.agregar_libro("Cien años de soledad", "Gabriel García Márquez", 19.99)
        self.builder.agregar_libro("Harry Potter y la piedra filosofal", "J.K. Rowling", 18.50)

    def obtener_pedido(self):
        return self.builder.obtener_pedido()


# Uso del Builder
tienda = Tienda()
builder = PedidoBuilder()
tienda.construir_pedido(builder)
pedido = tienda.obtener_pedido()
pedido.mostrar_pedido()

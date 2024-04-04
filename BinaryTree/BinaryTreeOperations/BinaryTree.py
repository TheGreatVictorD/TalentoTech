class Node:
    def __init__(self, value):
        # Inicializa un nodo con el valor que se recive como parámetro
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        # Inicializa un árbol binario con la raíz establecida en None
        self.root = None

    def insert(self, value):
        # Inserta un valor en el árbol binario
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        # Método privado para insertar recursivamente un valor en el árbol
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert_recursive(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert_recursive(current_node.right, value)

    def mostrar_arbol_bin(self, sangria=5):
        # Método para mostrar el árbol de forma jerárquica
        if self.root is None:
            print("El árbol está vacío!")
            return
        print("El árbol es:")
        self._mostrar_arbol_bin_rec(self.root, "", "", sangria)

    def _mostrar_arbol_bin_rec(self, nodo, prefijo_actual, prefijo_siguiente, sangria):
        # Método privado para mostrar el árbol de forma jerárquica con sangría
        if nodo is None:
            return

        print(prefijo_actual + str(nodo.value))

        if nodo.right is not None and nodo.left is not None:
            self._mostrar_arbol_bin_rec(nodo.right, prefijo_siguiente + "├" + "─" * sangria,
                                        prefijo_siguiente + "│" + " " * sangria, sangria)
            self._mostrar_arbol_bin_rec(nodo.left, prefijo_siguiente + "└" + "─" * sangria,
                                        prefijo_siguiente + " " * (sangria + 1), sangria)
        elif nodo.right is not None:
            self._mostrar_arbol_bin_rec(nodo.right, prefijo_siguiente + "├" + "─" * sangria,
                                        prefijo_siguiente + "│" + " " * sangria, sangria)
        elif nodo.left is not None:
            self._mostrar_arbol_bin_rec(nodo.left, prefijo_siguiente + "├" + "─" * sangria,
                                        prefijo_siguiente + "│" + " " * sangria, sangria)


# Ejemplo de uso
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)
tree.insert(10)
tree.insert(9)
tree.insert(12)
tree.insert(6.5)
tree.insert(5.8)

# Visualización jerárquica
print("Visualización jerárquica:")
tree.mostrar_arbol_bin()

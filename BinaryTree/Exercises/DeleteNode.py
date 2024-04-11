"""
Eliminar nodo: Escribir un método que elimine un nodo específico de un árbol binario.
"""

"""
Para eliminar un nodo específico de un árbol binario, se necesita un algoritmo que maneje varios casos:

Si el nodo a eliminar es una hoja (no tiene hijos), se puede eliminar directamente.
Si el nodo tiene solo un hijo, se puede reemplazar por su hijo.
Si el nodo tiene dos hijos, se puede reemplazar por el nodo sucesor (el nodo más pequeño en el subárbol derecho).
"""


class Node:
    def __init__(self, value):
        # Inicializa un nodo con el valor que se recibe como parámetro
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

    def eliminar_nodo(self, value):
        # Método para eliminar un nodo específico del árbol
        self.root = self._eliminar_nodo_rec(self.root, value)

    def _eliminar_nodo_rec(self, current_node, value):
        # Método privado para eliminar recursivamente un nodo del árbol
        if current_node is None:
            return current_node

        # Si el valor está en el subárbol izquierdo, recursivamente eliminamos en el subárbol izquierdo
        if value < current_node.value:
            current_node.left = self._eliminar_nodo_rec(current_node.left, value)
        # Si el valor está en el subárbol derecho, recursivamente eliminamos en el subárbol derecho
        elif value > current_node.value:
            current_node.right = self._eliminar_nodo_rec(current_node.right, value)
        # Si encontramos el nodo a eliminar
        else:
            # Caso 1: El nodo a eliminar no tiene hijos o solo tiene un hijo
            if current_node.left is None:
                temp = current_node.right
                current_node = None
                return temp
            elif current_node.right is None:
                temp = current_node.left
                current_node = None
                return temp

            # Caso 2: El nodo a eliminar tiene dos hijos
            # Encontramos el sucesor en el subárbol derecho (el menor valor en el subárbol derecho)
            temp = self.encontrar_sucesor(current_node.right)
            # Copiamos el valor del sucesor al nodo actual
            current_node.value = temp.value
            # Eliminamos el sucesor recursivamente
            current_node.right = self._eliminar_nodo_rec(current_node.right, temp.value)

        return current_node

    def encontrar_sucesor(self, current_node):
        # Método para encontrar el sucesor (menor valor) en el subárbol derecho
        while current_node.left is not None:
            current_node = current_node.left
        return current_node


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

# Eliminar el nodo con valor 7
tree.eliminar_nodo(7)
print("\nÁrbol después de eliminar el nodo con valor 7:")
tree.mostrar_arbol_bin()

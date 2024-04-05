"""
Recorrido inorden: Implementar un método para realizar un recorrido inorden de un árbol binario.
"""


class Node:
    def __init__(self, value):
        """Inicializa un nuevo nodo con el valor dado."""
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        """Inicializa un árbol binario vacío."""
        self.root = None

    def insert(self, value):
        """Inserta un nuevo nodo con el valor dado en el árbol."""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        """Función auxiliar recursiva para insertar un nuevo nodo en el árbol."""
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

    def inorder_traversal(self, node):
        """Realiza un recorrido inorden del árbol a partir del nodo dado."""
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.value, end=" ")
            self.inorder_traversal(node.right)


# Ejemplo de uso
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)

# Realiza e imprime el recorrido inorden del árbol
print("Recorrido inorden:")
tree.inorder_traversal(tree.root)

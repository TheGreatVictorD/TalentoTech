"""
Nivel de un nodo: Escribir un programa que devuelva el nivel de un nodo específico en un árbol binario.
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

    def get_node_level(self, node, target_value, level=1):
        """Obtiene el nivel del nodo con el valor dado en el árbol."""
        if node is None:
            return 0
        if node.value == target_value:
            return level
        left_level = self.get_node_level(node.left, target_value, level + 1)
        if left_level != 0:
            return left_level
        right_level = self.get_node_level(node.right, target_value, level + 1)
        return right_level


# Ejemplo de uso
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

# Obtener y mostrar el nivel de un nodo específico
target_node_value = 0
node_level = tree.get_node_level(tree.root, target_node_value)
if node_level != 0:
    print(f"El nivel del nodo con valor {target_node_value} es {node_level}.")
else:
    print(f"No se encontró el nodo con valor {target_node_value} en el árbol.")

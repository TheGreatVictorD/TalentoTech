from collections import deque
"""
Es árbol completo: Escribir un programa que verifique si un árbol binario es completo
(todos los nodos tienen 0 o 2 hijos).
"""

"""
Para verificar si un árbol binario es completo, puedes usar un enfoque de recorrido por niveles (BFS) 
y verificar que cada nodo tenga 0 o 2 hijos, a menos que sea una hoja en el último nivel. Aquí te muestro 
cómo se implementa:
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
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

    def is_complete(self):
        if self.root is None:
            return True

        queue = deque([self.root])
        leaf_found = False

        while queue:
            current_node = queue.popleft()

            if current_node.left:
                if leaf_found:
                    return False
                queue.append(current_node.left)
            else:
                leaf_found = True

            if current_node.right:
                if leaf_found:
                    return False
                queue.append(current_node.right)
            else:
                leaf_found = True

        return True


# Ejemplo de uso
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

print("El árbol es completo:", tree.is_complete())  # Debería imprimir True en este caso

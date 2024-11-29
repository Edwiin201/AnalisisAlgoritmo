class BinaryTreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if self.root is None:
            self.root = BinaryTreeNode(key)
        else:
            self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, root, key):
        if root.left is None:
            root.left = BinaryTreeNode(key)
        elif root.right is None:
            root.right = BinaryTreeNode(key)
        else:
            # Continuar en un nivel inferior (esto solo es un ejemplo para mostrar la inserción)
            self._insert_recursive(root.left, key)

    def display(self, root):
        if root:
            print(root.value)
            self.display(root.left)
            self.display(root.right)

# Crear el árbol binario completo y agregar elementos
tree = BinaryTree()
tree.insert(10)
tree.insert(20)
tree.insert(30)
tree.insert(40)
tree.insert(50)

# Imprimir el árbol
tree.display(tree.root)


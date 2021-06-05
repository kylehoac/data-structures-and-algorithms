class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        def walk(root, collection):
            if not root:
                return
            collection.append(root.value)
            walk(root.left, collection)
            walk(root.right, collection)

        collected_values = []
        walk(self.root,collected_values)

    def in_order(self):
        def walk(root, collection):
            if not root:
                return
            walk(root.left, collection)
            collection.append(root.value)
            walk(root.right, collection)

        collected_values = []
        walk(self.root,collected_values)
        pass

    def post_order(self):
        def walk(root, collection):
            if not root:
                return
            walk(root.left, collection)
            walk(root.right, collection)
            collection.append(root.value)

        collected_values = []
        walk(self.root,collected_values)
        pass

class BinarySearchTree(BinaryTree):
    def add(self, value):
        node = Node(value)

        def walk(root, node_to_add):
            value_to_add = node_to_add.value

            if not root:
                return
            if value_to_add < root.value:
                if root.left:
                    walk(root.left,node_to_add)
                else:
                    root.left = node_to_add
                    pass
            else:
                if root.right:
                    walk(root.right, node_to_add)
                else:
                    root.right = node_to_add

        if not self.root:
            self.root = Node(value)
            return

        walk(self.root, node)

    def contains(self, value):
        def walk(root, value):
            if not root:
                return False

            return (root.value == value or walk(root.left, value) or walk(root.right,value))

        walk(self.root, value)

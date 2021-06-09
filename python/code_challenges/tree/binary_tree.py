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

    def post_order(self):
        def walk(root, collection):
            if not root:
                return
            walk(root.left, collection)
            walk(root.right, collection)
            collection.append(root.value)

        collected_values = []
        walk(self.root,collected_values)

    def find_max_value(self):
        max_value = self.root.value
        def walk(root, max_value):
            if not root:
                return

            if root.value > max_value:
                max_value = root.value
            max_value = walk(root.left, max_value)
            max_value = walk(root.right, max_value)

        max_value = walk(self.root, max_value)
        return max_value

    def breadth_first(self,root):
        queue = []
        queue.append(root)
        if not root:
            return
        while not :


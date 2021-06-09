from collections import deque

class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        if self.dq:
            return self.dq.pop()
        else:
            return "queue is empty"

    def is_empty(self):
        return len(self.dq) == 0

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
        return collected_values
    def in_order(self):
        def walk(root, collection):
            if not root:
                return
            walk(root.left, collection)
            collection.append(root.value)
            walk(root.right, collection)

        collected_values = []
        walk(self.root,collected_values)
        return collected_values

    def post_order(self):
        def walk(root, collection):
            if not root:
                return
            walk(root.left, collection)
            walk(root.right, collection)
            collection.append(root.value)

        collected_values = []
        walk(self.root,collected_values)
        return collected_values

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

    @staticmethod
    def breadth_first(tree):
        queue_breadth = Queue()
        queue_breadth.enqueue(tree.root)
        values = []

        if not tree.root:
            return values

        while not queue_breadth.is_empty():
            front = queue_breadth.dequeue()
            values.append(front.value)
            if front.left:
                queue_breadth.enqueue(front.left)
            if front.right:
                queue_breadth.enqueue(front.right)

        return values

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

        return walk(self.root, value)

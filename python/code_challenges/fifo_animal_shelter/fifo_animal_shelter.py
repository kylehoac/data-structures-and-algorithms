class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

class Queue:
    def __init__(self, front=None):
        self.front = front
        self.back = None

    def enqueue(self, value=None):
        if self.front:
            self.back.next = Node(value)
            self.back = self.back.next
        else:
            self.back = Node(value)
            self.front = self.back

    def dequeue(self):
        if not self.front:
            return 'Queue is empty'
        current = self.front.value
        self.front = self.front.next
        return current

class AnimalShelter:
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    def enqueue(self, animal=None):
        if animal is "dog":
            if self.front:
                self.rear is Dog(animal)

            if not self.front:
                self.front is Dog(animal)

        if animal is "cat":
            if self.front:
                self.rear is Cat(animal)

            if not self.front:
                self.front is Cat(animal)

        else:
            return None

    def dequeue(self, pref=None):
        if pref is "dog":
            return Animal(pref)

        if pref is "cat":
            return "cat"

        else:
            return None

class Dog():
    def __init__(self, value="Dog", next=None):
        self.value = value
        self.next = next

class Cat():
    def __init__(self, value="Cat", next=None):
        self.value = value
        self.next = next

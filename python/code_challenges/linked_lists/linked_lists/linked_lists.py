class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def insert(self, value):
        self.head = Node(value, self.head)

    def include(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True

            current = current.next
            return False

    def get_all_values(self):
        list = []
        current = self.head

        while current:
            list.append(current.value)
            current = current.next

        return list

    def __str__(self):
        list = self.get_all_values()
        string = ""

        if list == []:
            string = "List is empty"
        elif list:
            string = ( " -> " ).join(list) + " -> None"

        return string

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    # def __str__(self):
    #     string = ""
    #     current = self.head

    #     while current:
    #         string = ( " -> " ).join(current.value)
    #         current = current.next

    #     return string

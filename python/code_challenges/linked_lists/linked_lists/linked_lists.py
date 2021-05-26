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

    def append(self, value):
        current = self.head

        while current:
            if current.next.value == None:
                current.next = Node(value)
                return

            current = current.next

    def insert_before(self, value, new_val):
        current = self.head

        while current:
            if current.next.value == value:
                old_next = current.next
                current.next = Node(new_val, old_next)
                return

            current = current.next

    def insert_after(self, value, new_val):
        current = self.head

        while current != None:
            if current.value == value:
                new_next = current.next
                current = Node(new_val, new_next)
                return

            current = current.next

    def kth_from_end(self, k):
        counter = 0
        leader = self.head
        follower = self.head

        while leader:
            if leader.next.value is not None:
                counter +=1
                leader = leader.next
                continue

            if k == counter:
                if leader.next.value is None:
                    return follower.value

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

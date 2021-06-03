from typing import OrderedDict


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
            if current.next == None:
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
        while current:
            if current.value == value:
                old_next = current.next
                current.next = Node(new_val, old_next)
                return

            current = current.next

    def kth_from_end(self, k):
        counter = 0
        leader = self.head
        follower = self.head

        while leader:
            if leader.next != None:
                counter +=1
                leader = leader.next
                return

            if k == counter:
                if leader.next.value == None:
                    return follower.value

    def reverse_list(self,list):
        prev = None
        current = self.head
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = current.next
        self.head = prev

        pass

def zip_list(lista,listb):
    current_a = lista.head
    current_b = listb.head

    while current_a and current_b:
        old_next_a = current_a.next
        old_next_b = current_b.next

        current_a.next = current_b
        if current_a != None:
            current_b.next = old_next_a

            current_a = old_next_a
            current_b = old_next_b
        else:
            break
    return lista

class Node:
    def __init__(self, value, next = None, previous = None):
        self.value = value
        self.next = next
        self.previous = previous

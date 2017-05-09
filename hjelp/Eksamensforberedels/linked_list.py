
class Node:

    next = None

    def __init__(self, data):
        self.data = data

    def append(self, data):
        current = self
        while current.next is not None:
            current = current.next
        current.next = Node(data)


class LinkedList:

    head = None

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(data)

    def prepend(self, data):
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head

    def delete_with_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next



class Node:
    """
    Node class
    """

    def __init__(self,value, next = None):
        self.next = next
        self.value = value


class LinkedList:
    """
    code to initialize, insert, and check linked list.
    """

    def __init__(self, head=None):
        self.head = head


    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node


    def insert_before(self, current, target):
        current = self.head
        while current:
            if current.next == target:


    def insert_after(self, value, target):
        pass
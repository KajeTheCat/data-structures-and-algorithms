

class Node:
    def __init__(self, next = None):
        self.next = next

class LinkedList:
    """
    code to initialize, insert, and check linked list.
    """

    def __init__(self, head=None):
        self.head = head


        def insert(self, value):
            node = Node(value)
            if self.head is not None:
                node.next = self.head
            self.head = node


        def insert_before(self, value, target):
            node = Node(value)
            if self.head is not None:
                node.next = self.head
            self.head = node


        def insert_after(self, value, target):
            node = Node(value)
            if self.head is not None:
                node.next = self.head
            self.head = node
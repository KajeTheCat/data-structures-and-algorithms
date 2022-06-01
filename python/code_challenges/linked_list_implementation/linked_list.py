class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    """
    code to initialize, insert, stringify, and check linked list.
    """

    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = Node(value)
        if self.head is not None:
            node.next = self.head
        self.head = node

    def to_string(self):
        if self.head is None:
            return "Null"
        

    def includes(self):
        pass

class TargetError:
    pass

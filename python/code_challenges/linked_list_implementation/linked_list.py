from platform import node


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

    def __str__(self):
        current = self.head
        str = ''
        while current:
            # "{ a } -> { b } -> { c } -> NULL"
            str += f'{{ {current.value} }} -> '
            current = current.next
        print(str)
        return str + "NULL"

    def insert(self, value):
        node = Node(value)
        if self.head is not None:
            node.next = self.head
        self.head = node

    def to_string(self):
        current = self.head
        str = ''
        while current:
            # "{ a } -> { b } -> { c } -> NULL"
            str += f'{ {current.value} } -> '
            current = current.next
        print(str)
        return str + "NULL"

    def includes(self, val):
        current = self.head
        while current:
            if current.value == val:
                return True
            current = current.next
        return False

class TargetError:
    pass

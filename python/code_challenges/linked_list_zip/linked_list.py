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

    def kth_from_end(self, value):		
        node = Node(value)
        length=0
        current = self.head
        while current:
            length += 1
            current = current.next
        length = length - value
        while  length != 0:
            length -= 1
        current = current.next
        return current.value



class TargetError:
    try:
        raise ValueError
    except ValueError:
        print("ValueError Exception!")

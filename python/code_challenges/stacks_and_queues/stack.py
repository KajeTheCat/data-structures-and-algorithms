from node import Node
from invalid_operation_error import InvalidOperationError

class Stack:
    """
    Functions to Push, Pop, Peek, and also return a Boolean if the stack is empty or not.
    """

    def __init__(self):
        self.top = None

    def __str__(self):
        current = self.top
        print(current.value)
        str = ''
        while current:
            str += f'{{ {current.value} }} -> '
            current = current.next
        return str + "NULL"

    def push(self, value):
        node = Node(value)
        if self.top is None:
            self.top = node
        else:
            temp = self.top
            self.top = node
            self.top.next = temp

    def pop(self):
        if self.top:
            temp = self.top
            self.top = self.top.next
            return temp.value
        else:
            raise InvalidOperationError

    def peek(self):
        if self.top:
            return self.top.value
        else:
            raise InvalidOperationError

    def is_empty(self):
        if self.top:
            return True
        else:
            return False


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.top.value)

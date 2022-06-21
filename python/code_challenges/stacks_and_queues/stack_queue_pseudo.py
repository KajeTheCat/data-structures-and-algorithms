from stack import Stack
from node import Node

class PseudoQueue:

    def __init__(self):
        self.stack = Stack()
        self.temp = Stack()

    def enqueue(self,value):
        if self.stack.is_empty():
            self.stack.push(value)
        else:
            while self.stack.is_empty() is False:
                self.temp.push(self.stack.pop())
            self.stack.push(value)
            while self.temp.is_empty() is False:
                self.stack.push(self.temp.pop())

    def dequeue(self):
        return self.stack.pop()

class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self):
        # method body here
        pass

    def dequeue(self):
        # method body here
        pass

    def peek(self):
        if self.front:
            return self.front.value
        else:
            raise InvalidOperationError

    def is_empty(self):
        if self.front:
            return True
        else:
            return False

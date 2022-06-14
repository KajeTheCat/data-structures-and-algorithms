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


def zip_lists(llist1, llist2):
    if(llist1.head == None and llist2.head == None):
        raise TargetError
    if(llist1.head == None and llist2.head):
        return llist2
    if(llist1.head and llist2.head == None):
        return llist1

    current1 = llist1.head
    current2 = llist2.head

    while current1 and current2:

        temp1 = current1.next
        temp2 = current2.next

        current2.next = temp1
        current1.next = current2

        current1 = temp1
        current2 = temp2

        llist2.head = current2
    return llist1


class TargetError(Exception):
    def __init__(self):
        self.message = "Whatever"

    def __str__(self):
        return self.message

if __name__ == "__main__":
    a = LinkedList()
    b = LinkedList()
    a.insert(2)
    a.insert(1)
    # a.insert(5)
    b.insert('c')
    b.insert('b')
    b.insert('a')
    print(a)
    print(b)
    print(zip_lists(a,b))

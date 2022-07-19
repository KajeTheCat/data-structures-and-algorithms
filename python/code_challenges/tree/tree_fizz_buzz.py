from binary_tree import BinaryTree
from queue import Queue
from kary_tree import Node

def fizz_buzz_tree(tree, Node = None):
    new_tree = tree
    if not tree.root:
        return "no tree found"

    queue = Queue()

    queue.enqueue(new_tree.root)

    while not queue.is_empty():
        node = queue.dequeue()
        if node.value % 15 == 0:
            node.value = "FizzBuzz"
        elif node.value % 3 == 0:
            node.value = "Fizz"
        elif node.value % 5 == 0:
            node.value = "Buzz"
        else:
            node.value = str(node.value)

        for child in node.children:
            queue.enqueue(child)

    return new_tree


if __name__ == "__main__":
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(8)
    nine = Node(9)
    ten = Node(10)
    eleven = Node(11)
    twelve = Node(12)
    thirteen = Node(13)
    fourteen = Node(14)
    fifteen = Node(15)

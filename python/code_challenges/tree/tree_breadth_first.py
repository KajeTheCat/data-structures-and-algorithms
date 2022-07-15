from binary_tree import BinaryTree, Node


def breadth_first(tree):

    queue = []

    horizontal = []

    current = tree.root

    queue.append(current)

    while len(queue) > 0:
        current = queue.pop(0)

        if current is None:
            return []

        horizontal.append(current.value)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    return horizontal


if __name__ == "__main__":
    # outcome [a,b,c,e,f,g]

    b = BinaryTree()
    b.root = Node("a")
    b.root.left = Node("b")
    b.root.right = Node("c")
    b.root.left.left = Node("d")
    b.root.left.right = Node("e")
    b.root.right.left = Node("f")
    b.root.right.right = Node("g")

    print(breadth_first(b))

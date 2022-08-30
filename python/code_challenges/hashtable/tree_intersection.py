from .binary_tree import BinaryTree, Node
from .hashtable import Hashtable


def tree_intersection(tree_a, tree_b):
    if tree_a == None or tree_b == None:
        return None
    ap = tree_a.pre_order()
    bp = tree_b.pre_order()

    apbp_sum = ap+bp

    h = Hashtable()
    container = []
    for item in apbp_sum:
        if h.contains(item) and item not in container:
            container.append(item)
        else:
            h._set(item, item)
    return container


if __name__ == "__main__":
    tree_a = BinaryTree()
    a = Node(1)
    b = Node(2)
    c = Node(3)
    g = Node(4)
    h = Node(6)
    i = Node(8)
    j = Node(9)
    tree_a.root = a
    tree_a.root.left = b
    tree_a.root.right = c
    tree_a.root.left.left = g
    tree_a.root.left.right = h
    tree_a.root.right.right = i
    tree_a.root.right.left = j
    tree_b = BinaryTree()
    d = Node(3)
    e = Node(4)
    f = Node(5)
    k = Node(9)
    l = Node(6)
    m = Node(2)
    tree_b.root = d
    tree_b.root.left = e
    tree_b.root.right = f
    tree_b.root.left.right = k
    tree_b.root.left.left = l
    tree_b.root.right.left = m

    tree_intersection(tree_a, tree_b)

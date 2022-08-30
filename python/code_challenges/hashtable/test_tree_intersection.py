import pytest
from .tree_intersection import tree_intersection
from .binary_tree import BinaryTree, Node
from .hashtable import Hashtable
from tree.queue import Queue


def test_exists():
    assert tree_intersection


# @pytest.mark.skip("TODO")
def test_tree_intersection():

    tree_a = BinaryTree()
    values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
    add_values_to_empty_tree(tree_a, values)

    tree_b = BinaryTree()
    values = [42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500]
    add_values_to_empty_tree(tree_b, values)

    actual = tree_intersection(tree_a, tree_b)
    expected = [125, 175, 100, 160, 500, 200, 350]

    assert sorted(actual) == sorted(expected)

def test_empty():
    tree_a = BinaryTree
    tree_a = None
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

    actual = tree_intersection(tree_a, tree_b)
    expected = None

    assert actual == expected


def add_values_to_empty_tree(tree, values):
    """
    Helper function to add given values to BinaryTree
    """
    tree.root = Node(values.pop())
    q = Queue()

    q.enqueue(tree.root)

    while values:
        node = q.dequeue()
        node.left = Node(values.pop())
        node.right = Node(values.pop()) if values else None
        q.enqueue(node.left)
        q.enqueue(node.right)

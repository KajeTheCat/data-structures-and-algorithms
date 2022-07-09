class BinaryTree:
    """
    Class for the pre_order, in_order, and post_order methods.
    """

    def __init__(self):
        # initialization here
        pass

    def pre_order(self):

        def walk(root):

            if not root:
                return

            values.append(root.value)

            walk(root.left)

            walk(root.right)

        values = []
        walk(self.root)

        return values

    def in_order(self):

        def walk(root):

            if not root:
                return

            walk(root.left)

            values.append(root.value)

            walk(root.right)

        values = []
        walk(self.root)

        return values

    def post_order(self):

        def walk(root):

            if not root:
                return

            walk(root.left)

            walk(root.right)

            values.append(root.value)

        values = []
        walk(self.root)

        return values


class Node:
    def __init__(self, value,left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node {self.value}"

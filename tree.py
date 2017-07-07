class Node:

    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


class BST:
    """
    minimal BST. Only supports insert
    """
    def __init__(self, root=None):
        self.root = root

    def insert(self, val):
        self.root = self._insert(val, self.root)

    def _insert(self, val, r):
        if r is None:
            r = Node(val)
            return r

        if val > r.val:
            r.right = self._insert(val, r.right)
        elif val < r.val:
            r.left = self._insert(val, r.left)

        return r

    def __iter__(self):
        return self.root.__iter__()

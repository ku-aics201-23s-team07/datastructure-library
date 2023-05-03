import math

class AVLNode:
    def __init__(self, location):
        self.location = location
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, location):
        self.root = self._insert(self.root, location)

    def _insert(self, node, location):
        if node is None:
            node = AVLNode(location)
        elif location['latitude'] < node.location['latitude']:
            node.left = self._insert(node.left, location)
            if self._height(node.left) - self._height(node.right) == 2:
                if location['latitude'] < node.left.location['latitude']:
                    node = self._rotate_right(node)
                else:
                    node = self._rotate_left_right(node)
        elif location['latitude'] > node.location['latitude']:
            node.right = self._insert(node.right, location)
            if self._height(node.right) - self._height(node.left) == 2:
                if location['latitude'] > node.right.location['latitude']:
                    node = self._rotate_left(node)
                else:
                    node = self._rotate_right_left(node)

        node.height = max(self._height(node.left), self._height(node.right)) + 1
        return node

    def search(self, location):
        return self._search(self.root, location)

    def _search(self, node, location):
        if node is None:
            return None
        elif node.location['latitude'] == location['latitude']:
            return node
        elif self._distance(location, node.location) < self._distance(location, node.left.location):
            return self._search(node.left, location)
        else:
            return self._search(node.right, location)

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _balance(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _rotate_right(self, node):
        left_child = node.left
        left_grandchild = left_child.right
        left_child.right = node
        node.left = left_grandchild
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        left_child.height = 1 + \
            max(self._height(left_child.left), self._height(left_child.right))
        return left_child

    def _rotate_left(self, node):
        right_child = node.right
        right_grandchild = right_child.left
        right_child.left = node
        node.right = right_grandchild
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        right_child.height = 1 + \
            max(self._height(right_child.left), self._height(right_child.right))
        return right_child

    def _distance(self, location1, location2):
        if location1 is None or location2 is None:
            return float('inf')
        return math.sqrt((location1['latitude'] - location2['latitude'])**2 + (location1['longitude'] - location2['longitude'])**2)
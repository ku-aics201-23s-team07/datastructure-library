import math
from haversine import haversine
from graphviz import Digraph

class LocationAVLNode:
    def __init__(self, inputData):
        self.locationId = inputData['location_id']
        self.locationName = inputData['name']
        self.location = { 
            "latitude": inputData['latitude'], 
            "longitude": inputData['longitude']
        }
        self.scooters = inputData['scooters']
        self.left = None
        self.right = None
        self.height = 1

class LocationAVLTree:
    def __init__(self):
        self.root = None

    def insert(self, location):
        self.root = self._insert(self.root, location)

    def _insert(self, node, location):
        if node is None:
            node = LocationAVLNode(location)
        elif location['location_id'] < node.locationId:
            node.left = self._insert(node.left, location)
            if self._height(node.left) - self._height(node.right) == 2:
                if location['location_id'] < node.left.locationId:
                    node = self._rotate_right(node)
                else:
                    node = self._rotate_left_right(node)
        elif location['location_id'] > node.locationId:
            node.right = self._insert(node.right, location)
            if self._height(node.right) - self._height(node.left) == 2:
                if location['location_id'] > node.right.locationId:
                    node = self._rotate_left(node)
                else:
                    node = self._rotate_right_left(node)

        node.height = max(self._height(node.left), self._height(node.right)) + 1
        return node
    
    def delete(self, locationId):
        self.root = self._delete(self.root, locationId)

    def _delete(self, node, locationId):
        if node is None:
            return None

        if locationId < node.locationId:
            node.left = self._delete(node.left, locationId)
        elif locationId > node.locationId:
            node.right = self._delete(node.right, locationId)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._find_minimum(node.right)
                node.locationId = successor.locationId
                node.locationName = successor.locationName
                node.location = successor.location
                node.scooters = successor.scooters
                node.right = self._delete(node.right, successor.locationId)

        node.height = max(self._height(node.left), self._height(node.right)) + 1

        balance = self._get_balance(node)
        if balance > 1:
            if self._get_balance(node.left) >= 0:
                return self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                return self._rotate_right(node)
        elif balance < -1:
            if self._get_balance(node.right) <= 0:
                return self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                return self._rotate_left(node)

        return node
    
    def search(self, locationId):
        return self._search(self.root, locationId)

    def _search(self, node, locationId):
        if node is None:
            return None
        if node.locationId == locationId:
            return node
        elif locationId < node.locationId:
            return self._search(node.left, locationId)
        else:
            return self._search(node.right, locationId)

    def _find_minimum(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _get_balance(self, node):
        if node is None:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _rotate_right(self, node):
        left_child = node.left
        left_grandchild = left_child.right
        left_child.right = node
        node.left = left_grandchild
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        left_child.height = 1 + max(self._height(left_child.left), self._height(left_child.right))
        return left_child

    def _rotate_left(self, node):
        right_child = node.right
        right_grandchild = right_child.left
        right_child.left = node
        node.right = right_grandchild
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        right_child.height = 1 + max(self._height(right_child.left), self._height(right_child.right))
        return right_child

    def _rotate_left_right(self, node):
        node.left = self._rotate_left(node.left)
        return self._rotate_right(node)

    def _rotate_right_left(self, node):
        node.right = self._rotate_right(node.right)
        return self._rotate_left(node)

    def _distance(self, location1, location2):
        if location1 is None or location2 is None:
            return float('inf')
        return haversine((location1['latitude'], location1['longitude']), (location2['latitude'], location2['longitude']), unit="m")
    
    def find_nearest_location(self, user_location):
        nearest_location = None
        min_distance = float('inf')

        stack = []
        curr = self.root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                distance = self._distance(curr.location, user_location)
                if distance < min_distance:
                    min_distance = distance
                    nearest_location = curr
                curr = curr.right

        return nearest_location, min_distance
    
    def _visualize(self, node, dot):
        if node is None:
            return

        dot.node(str(id(node)), str(node.locationId))

        if node.left is not None:
            dot.edge(str(id(node)), str(id(node.left)), label="L")
            self._visualize(node.left, dot)

        if node.right is not None:
            dot.edge(str(id(node)), str(id(node.right)), label="R")
            self._visualize(node.right, dot)

    def visualize(self):
        try:
            dot = Digraph()
            self._visualize(self.root, dot)
            return dot
        except Exception as ex:
            print(ex)
import math
from haversine import haversine

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
        elif location['name'] < node.locationName:
            node.left = self._insert(node.left, location)
            if self._height(node.left) - self._height(node.right) == 2:
                if location['name'] < node.left.locationName:
                    node = self._rotate_right(node)
                else:
                    node = self._rotate_left_right(node)
        elif location['name'] > node.locationName:
            node.right = self._insert(node.right, location)
            if self._height(node.right) - self._height(node.left) == 2:
                if location['name'] > node.right.locationName:
                    node = self._rotate_left(node)
                else:
                    node = self._rotate_right_left(node)

        node.height = max(self._height(node.left), self._height(node.right)) + 1
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
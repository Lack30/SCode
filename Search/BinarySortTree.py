
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class DictBinTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def search(self, key):
        bt = self.root
        while bt is not None:
            entry = bt.data
            if key < entry.data:
                bt = bt.left
            elif key > entry.data:
                bt = bt.right
            else:
                return entry.data
        return None

    def insert(self, key):
        bt = self.root
        
class aBST:

    def __init__(self, depth):
        tree_size = pow(2, depth) - 1
        self.Tree = [None] * tree_size

    def FindKeyIndex(self, key):
        index = 0
        while index < len(self.Tree):
            if self.Tree[index] is None:
                return -index
            if self.Tree[index] == key:
                return index
            if self.Tree[index] > key:
                index = 2 * index + 1
                continue
            if self.Tree[index] < key:
                index = 2 * index + 2
                continue
        return None

    def AddKey(self, key):
        index = self.FindKeyIndex(key)
        if index is None:
            return -1
        if index == 0 and self.Tree[index] is None:
            self.Tree[0] = key
            return index
        if index == 0 and self.Tree[index] == key:
            return index
        if index < 0:
            index = -index
            self.Tree[index] = key
        return index

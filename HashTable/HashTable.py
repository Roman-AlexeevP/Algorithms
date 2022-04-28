class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        return sum(bytearray(value, "utf-8")) % self.size

    def seek_slot(self, value):
        if self.size < 1 or self.step < 1:
            return None
        index = self.hash_fun(value)
        if self.slots[index] is None:
            return index
        new_index = (index + self.step) % self.size
        while new_index != index:
            if self.slots[new_index] is None:
                return new_index
            new_index = (new_index + self.step) % self.size

        return None

    def put(self, value):
        index = self.seek_slot(value)
        if index is not None:
            self.slots[index] = value
            return index
        return None

    def find(self, value):
        if self.size < 1 or self.step < 1:
            return None
        index = self.hash_fun(value)
        if self.slots[index] == value:
            return index
        new_index = (index + self.step) % self.size
        while new_index != index:
            if self.slots[new_index] == value:
                return new_index
            new_index = (new_index + self.step) % self.size

        return None

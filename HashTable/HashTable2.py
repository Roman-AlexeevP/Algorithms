class HashTable2:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        return sum(bytearray(value, "utf-8")) % self.size

    def hash_fun_second(self, value):
        return len(value) % 19

    def seek_slot(self, value):
        index = self.hash_fun(value)
        if self.slots[index] is None:
            return index
        for i in range(1, self.size):
            index = (index + i * self.hash_fun_second(value)) % self.size
            if self.slots[index] is None:
                return index

        return None

    def put(self, value):
        index = self.seek_slot(value)
        if index is not None:
            self.slots[index] = value
        return None

    def find(self, value):
        index = self.hash_fun(value)
        if self.slots[index] == value:
            return index
        for i in range(1, self.size):
            index = (index + i * self.hash_fun_second(value)) % self.size
            if self.slots[index] == value:
                return index
        return None

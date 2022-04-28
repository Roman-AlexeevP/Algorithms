class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.step = (self.size // 10) + 1

    def hash_fun(self, key):
        return sum(bytearray(key, "utf-8")) % self.size

    def seek_slot(self, key):
        if self.size < 1:
            return None
        index = self.hash_fun(key)
        if self.slots[index] is None:
            return index
        new_index = (index + self.step) % self.size
        while new_index != index:
            if self.slots[new_index] is None:
                return new_index
            new_index = (new_index + self.step) % self.size

        return None

    def is_key(self, key):
        return True if self.find(key) is not None else False

    def get(self, key):
        key_index = self.find(key)
        if key_index is not None:
            return self.values[key_index]
        return None

    def put(self, key, value):

        index = self.find(key)
        if index is not None:
            self.values[index] = value
            return index
        index = self.seek_slot(key)
        if index is not None:
            self.slots[index] = key
            self.values[index] = value
            return index
        return None

    def find(self, key):
        if self.size < 1:
            return None
        index = self.hash_fun(key)
        if self.slots[index] == key:
            return index
        new_index = (index + self.step) % self.size
        while new_index != index:
            if self.slots[new_index] == key:
                return new_index
            new_index = (new_index + self.step) % self.size
        return None

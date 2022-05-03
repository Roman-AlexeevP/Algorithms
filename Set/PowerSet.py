
class PowerSet:

    def __init__(self):
        self.items = dict()

    def size(self):
        return len(self.items)

    def put(self, value):
        if self.get(value):
            return None
        self.items[value] = value
        return value

    def get(self, value):
        if self.items.get(value) is not None:
            return True
        return False

    def remove(self, value):
        if self.get(value):
            del self.items[value]
            return True
        return False

    def intersection(self, set2):
        result = PowerSet()
        if set2 is None:
            return result
        for value in self.items:
            if set2.get(value):
                result.put(value)
        return result

    def union(self, set2):
        if set2.size() == 0 or set2 is None:
            return self
        for value in set2.items:
            self.put(value)
        return self

    def difference(self, set2):
        result = PowerSet()
        if set2 is None:
            return result
        for value in self.items:
            if not set2.get(value):
                result.put(value)
        return result

    def issubset(self, set2):
        if set2.size() == 0 or set2 is None:
            return False
        for val in set2.items:
            if not self.get(val):
                return False
        return True

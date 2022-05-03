
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
        result = PowerSet()
        for value in self.items:
            result.put(value)
        for value in set2.items:
            result.put(value)
        return result

    def difference(self, set2):
        result = PowerSet()
        if set2 is None:
            return result
        for value in self.items:
            if not set2.get(value):
                result.put(value)
        return result

    def issubset(self, set2):
        result = True
        for value in set2.items:
            if not self.get(value):
                result = False
                break
        return result

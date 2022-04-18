class Deque:
    def __init__(self):
        self.storage = []

    def addFront(self, item):
        self.storage.insert(0, item)

    def addTail(self, item):
        self.storage.append(item)

    def removeFront(self):
        if not self.storage:
            return None
        return self.storage.pop(0)

    def removeTail(self):
        if not self.storage:
            return None
        return self.storage.pop()

    def size(self):
        return len(self.storage)
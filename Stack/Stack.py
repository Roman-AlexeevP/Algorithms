class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None

    def push(self, value):
        return self.stack.append(value)

    def peek(self):
        if self.stack:
            return self.stack[self.size()-1]
        return None

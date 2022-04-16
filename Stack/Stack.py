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


class StackHead():
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.stack:
            return self.stack.pop(0)
        return None

    def push(self, value):
        self.stack.insert(0, value)

    def peek(self):
        if self.stack:
            return self.stack[0]
        return None

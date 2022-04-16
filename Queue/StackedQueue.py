from Stack.Stack import Stack

class StackedQueue():
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def enqueue(self, item):
        self.stack_in.push(item)

    def dequeue(self):
        if self.stack_out.size() < 1:
            while self.stack_in.size() > 0:
                value = self.stack_in.pop()
                self.stack_out.push(value)
        return self.stack_out.pop()

    def size(self):
        return self.stack_in.size() + self.stack_out.size()


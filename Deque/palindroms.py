from Deque import Deque

def is_palindrom(string):
    deque = Deque()

    for letter in string:
        deque.addFront(letter)

    while deque.size():
        if deque.removeTail() != string[deque.size()]:
            return False
return True

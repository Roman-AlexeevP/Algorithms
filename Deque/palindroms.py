from Deque import Deque

def is_palindrom(string):
    deque = Deque()

    for letter in string:
        deque.addFront(letter)

    for letter in string:
        if deque.removeFront() != letter:
            return False
    return True

from Deque import Deque

def is_palindrom(string):
    deque = Deque()

    for letter in string:
        deque.addFront(letter)

    while deque.size() > 1:
        if deque.removeTail() != deque.removeFront():
            return False
return True

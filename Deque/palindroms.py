from Deque import Deque

def is_palindrom(string):
    deque_front = Deque()
    deque_tail = Deque()

    for letter in string:
        deque_front.addFront(letter)
        deque_tail.addTail(letter)

    while deque_tail.size() > 0:
        if deque_front.removeTail() != deque_tail.removeTail():
            return False
    return True

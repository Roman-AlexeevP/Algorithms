from unittest import TestCase

from Deque import Deque

class TestDeque(TestCase):
    def setUp(self) -> None:
        self.deque = Deque()

    def test_add_front(self):
        self.deque.addFront(10)
        self.assertEqual(self.deque.size(), 1)
        self.assertIn(10, self.deque.storage)

    def test_add_tail(self):
        self.deque.addFront(20)
        self.deque.addFront(30)
        self.assertEqual(self.deque.size(), 2)
        self.assertIn(20, self.deque.storage)
        self.assertIn(30, self.deque.storage)
        self.assertEqual(self.deque.removeTail(), 20)
        self.assertEqual(self.deque.removeFront(), 30)

    def test_remove_front(self):
        self.deque.addFront(5)
        self.deque.addFront(10)
        self.deque.addTail(15)
        self.assertEqual(self.deque.size(), 3)
        self.assertEqual([10, 5, 15], self.deque.storage)
        self.assertEqual(self.deque.removeFront(), 10)
        self.assertEqual(self.deque.removeFront(), 5)
        self.assertEqual(self.deque.removeFront(), 15)

    def test_remove_tail(self):
        self.deque.addTail(15)
        self.deque.addTail(20)
        self.deque.addTail(25)
        self.deque.addFront(35)
        self.assertEqual(self.deque.size(), 4)
        self.assertEqual([35, 15, 20, 25], self.deque.storage)
        self.assertEqual(self.deque.removeTail(), 25)
        self.assertEqual(self.deque.removeTail(), 20)
        self.assertEqual(self.deque.removeTail(), 15)
        self.assertEqual(self.deque.removeTail(), 35)

    def test_size(self):
        self.deque.addFront(10)
        self.deque.addFront(20)
        self.deque.addTail(30)
        self.deque.addTail(40)
        self.assertEqual(len(self.deque.storage), 4)
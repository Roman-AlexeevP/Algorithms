from unittest import TestCase

from Queue import Queue
from StackedQueue import StackedQueue


class TestQueue(TestCase):

    def setUp(self) -> None:
        self.queue = Queue()

    def test_enqueue(self):
        for i in range(10):
            self.queue.enqueue(i)
        for i in range(10):
            self.assertEqual(self.queue.queue[i], i)

    def test_dequeue(self):
        for i in range(10):
            self.queue.enqueue(i)
        self.assertEqual(self.queue.dequeue(), 0)
        self.assertEqual(self.queue.size(), 9)

class StackedQueueTest(TestCase):

    def setUp(self) -> None:
        self.queue = StackedQueue()

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.size(), 1)
        self.assertEqual(self.queue.stack_in.size(), 1)
        self.assertEqual(self.queue.stack_out.size(), 0)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size(), 2)
        self.assertEqual(self.queue.stack_in.size(), 2)
        self.assertEqual(self.queue.stack_out.size(), 0)

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.size(), 0)

    def test_dequeue_2(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.queue.enqueue(4)
        self.queue.enqueue(5)
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertEqual(self.queue.dequeue(), 4)
        self.assertEqual(self.queue.size(), 1)
        self.assertEqual(self.queue.dequeue(), 5)
        self.assertEqual(self.queue.size(), 0)
        self.assertIsNone(self.queue.dequeue())
from unittest import TestCase

from LinkedList import LinkedList, Node
from LinkedListsSum import sum_two_list


class Test(TestCase):

    def setUp(self) -> None:
        self.ls1 = LinkedList()
        self.ls2 = LinkedList()

    def test_sum_two_list(self):
        node = Node(1)
        self.ls1.add_in_tail(node)
        self.ls2.add_in_tail(node)
        sum_ls = sum_two_list(self.ls1, self.ls2)
        self.assertEqual(sum_ls.len(), 1)
        self.assertEqual(sum_ls.head.value, 2)

    def test_sum_two_empty_list(self):
        sum_ls = sum_two_list(self.ls1, self.ls2)
        self.assertEqual(sum_ls.len(), 0)
        self.assertIsNone(sum_ls.head)
        self.assertIsNone(sum_ls.tail)
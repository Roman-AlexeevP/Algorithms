from unittest import TestCase

from LinkedList2 import LinkedList2, Node


class TestLinkedList2(TestCase):

    def setUp(self) -> None:


        self.empty_list = LinkedList2()

        self.test_node = Node(1)
        self.list_with_one_element = LinkedList2()
        self.list_with_one_element.add_in_tail(self.test_node)

        list_nodes = [Node(i) for i in range(1, 11)]
        self.filled_list = LinkedList2()
        for node in list_nodes:
            self.filled_list.add_in_tail(node)


    def test_find_all_empty(self):
        self.assertIsNone(self.empty_list.find(1))


    def test_delete_empty(self):
        self.empty_list.delete(4)

    def test_delete_one(self):
        self.list_with_one_element.delete(1)
        self.assertEqual(self.list_with_one_element.len(), 0)
        self.assertIsNone(self.list_with_one_element.head)
        self.assertIsNone(self.list_with_one_element.tail)

    def test_delete_filled(self):
        self.filled_list.delete(5)
        self.assertEqual(self.filled_list.len(), 9)
        self.assertIsNone(self.filled_list.head.prev)
        self.assertIsNone(self.filled_list.tail.next)
        node = self.filled_list.find(4)
        next_node = self.filled_list.find(6)
        self.assertEqual(node.next, next_node)
        self.assertEqual(next_node.prev, node)

    def test_delete_all(self):
        self.list_with_one_element.add_in_tail(Node(1))
        self.list_with_one_element.delete(1, all=True)
        self.assertEqual(self.list_with_one_element.len(), 0)
        self.assertIsNone(self.list_with_one_element.head)
        self.assertIsNone(self.list_with_one_element.tail)

    def test_delete_all_filled(self):
        self.filled_list.add_in_tail(Node(1))
        self.filled_list.insert(afterNode=self.filled_list.find(5), newNode=Node(1))
        self.filled_list.delete(1, all=True)
        self.assertEqual(self.filled_list.len(), 9)
        self.assertIsNotNone(self.filled_list.head)
        self.assertIsNotNone(self.filled_list.tail)
        self.assertEqual(self.filled_list.head.value, 2)
        self.assertEqual(self.filled_list.tail.value, 10)


    def test_clean_empty(self):

        self.empty_list.clean()
        self.assertEqual(self.empty_list.len(), 0)
        self.assertIsNone(self.empty_list.head)
        self.assertIsNone(self.empty_list.tail)


    def test_clean_one(self):
        self.list_with_one_element.clean()
        self.assertEqual(self.list_with_one_element.len(), 0)
        self.assertIsNone(self.list_with_one_element.head)
        self.assertIsNone(self.list_with_one_element.tail)

    def test_clean_filled(self):
        self.filled_list.clean()
        self.assertEqual(self.filled_list.len(), 0)
        self.assertIsNone(self.filled_list.head)
        self.assertIsNone(self.filled_list.tail)

    def test_len_empty(self):
        self.assertEqual(self.empty_list.len(), 0)

    def test_len_one(self):
        self.assertEqual(self.list_with_one_element.len(), 1)

    def test_len_filled(self):
        self.assertEqual(self.filled_list.len(), 10)

    def test_insert_empty(self):

        self.empty_list.insert(afterNode=None, newNode=self.test_node)
        self.assertEqual(self.empty_list.len(), 1)
        self.assertEqual(self.empty_list.head.value, 1)
        self.assertIsNone(self.empty_list.head.prev)
        self.assertIsNone(self.empty_list.tail.next)

    def test_insert_one(self):
        node=Node(5)
        self.list_with_one_element.insert(afterNode=None, newNode=node)
        self.assertEqual(self.list_with_one_element.len(), 2)
        self.assertEqual(self.list_with_one_element.head.value, 1)
        self.assertEqual(self.list_with_one_element.head.next, self.list_with_one_element.tail)
        self.assertIsNone(self.list_with_one_element.head.prev)
        self.assertIsNone(self.list_with_one_element.tail.next)
        self.assertEqual(self.list_with_one_element.tail.value, 5)


    def test_insert_filled(self):
        node = Node(33)
        self.filled_list.insert(
            afterNode=self.filled_list.find(5),
            newNode=node
        )
        self.assertIsNotNone(self.filled_list.find(33))
        self.assertEqual(self.filled_list.len(), 11)
        self.assertEqual(self.filled_list.find(5).next.value, 33)
        self.assertEqual(self.filled_list.find(6).prev.value, 33)

    def test_insert_filled_2(self):
        node = Node(33)
        self.filled_list.insert(
            afterNode=self.filled_list.find(10),
            newNode=node
        )
        self.assertIsNotNone(self.filled_list.find(33))
        self.assertEqual(self.filled_list.len(), 11)
        self.assertEqual(self.filled_list.tail, node)
        self.assertIsNone(self.filled_list.tail.next)

    def test_insert_non_empty(self):
        self.list_with_one_element.insert(afterNode=self.list_with_one_element.tail, newNode=Node(5))


    def test_add_in_head_empty(self):

        self.empty_list.add_in_head(self.test_node)
        self.assertEqual(self.empty_list.head.value, 1)
        self.assertEqual(self.empty_list.tail.value, 1)
        self.assertIsNone(self.empty_list.head.next)
        self.assertIsNone(self.empty_list.head.prev)
        self.assertIsNone(self.empty_list.tail.next)
        self.assertIsNone(self.empty_list.tail.prev)

    def test_add_in_head_one(self):
        node = Node(2)
        self.list_with_one_element.add_in_head(node)
        self.assertEqual(self.list_with_one_element.len(), 2)
        self.assertEqual(self.list_with_one_element.head.value, 2)
        self.assertEqual(self.list_with_one_element.head.next.value, 1)
        self.assertEqual(self.list_with_one_element.tail.value, 1)
        self.assertEqual(self.list_with_one_element.tail.prev.value, 2)
        self.assertIsNone(self.list_with_one_element.head.prev)
        self.assertIsNone(self.list_with_one_element.tail.next)

    def test_add_in_head_filled(self):
        node = Node(2)
        self.filled_list.add_in_head(node)
        self.assertEqual(self.filled_list.len(), 11)
        self.assertEqual(self.filled_list.head.value, 2)
        self.assertEqual(self.filled_list.head.next.value, 1)
        self.assertIsNone(self.filled_list.head.prev)
        self.assertIsNone(self.filled_list.tail.next)

from unittest import TestCase

from LinkedList import LinkedList, Node


class TestLinkedList(TestCase):

    def setUp(self) -> None:
        self.empty_list = LinkedList()
        self.list_with_data = LinkedList()
        self.list_with_one_element = LinkedList()

        self.list_with_data.add_in_tail(Node(1))
        self.list_with_data.add_in_tail(Node(2))
        self.list_with_data.add_in_tail(Node(3))
        self.list_with_data.add_in_tail(Node(2))
        self.list_with_data.add_in_tail(Node(4))

        self.list_with_one_element.add_in_tail(Node(1))


    def test_find_all(self):
        self.assertEqual(self.empty_list.find_all(2), [])
        nodes = self.list_with_data.find_all(2)
        self.assertEqual(len(nodes), 2)
        self.assertEqual(self.list_with_one_element.find_all(2), [])
        one_node_list = self.list_with_one_element.find_all(1)
        self.assertEqual(len(one_node_list), 1)
        self.assertEqual(one_node_list[0].value, 1)


    def test_delete_one_element_list(self):
        self.list_with_one_element.delete(1)
        self.assertEqual(self.list_with_one_element.len(), 0)
        self.assertIsNone(self.list_with_one_element.head)
        self.assertIsNone(self.list_with_one_element.tail)

    def test_delete_empty(self):
        self.assertFalse(self.empty_list.delete(6))
        self.assertEqual(self.empty_list.len(), 0)

    def test_delete_all(self):
        self.list_with_data.delete(2, all=True)
        self.assertEqual(self.list_with_data.len(), 3)
        self.assertEqual(self.list_with_data.head.value, 1)
        self.assertEqual(self.list_with_data.tail.value, 4)
        self.assertEqual(self.list_with_data.head.next.value, 3)

    def test_delete_all_two_elements(self):
        ls = LinkedList()
        n1 = Node(1)
        n2 = Node(1)
        ls.add_before_head(n1)
        ls.add_in_tail(n2)
        ls.delete(1, all=True)
        self.assertEqual(ls.len(), 0)
        self.assertIsNone(ls.tail)
        self.assertIsNone(ls.head)

    def test_delete_all_one_element(self):
        self.list_with_one_element.delete(1, all=True)
        self.assertEqual(self.list_with_one_element.len(), 0)
        self.assertIsNone(self.list_with_one_element.tail)
        self.assertIsNone(self.list_with_one_element.head)

    def test_delete_with_data(self):
        self.list_with_data.delete(4)
        self.assertEqual(self.list_with_data.len(), 4)
        self.assertEqual(self.list_with_data.head.value, 1)
        self.assertEqual(self.list_with_data.tail.value, 2)
        self.assertIsNone(self.list_with_data.tail.next)
        self.list_with_data.delete(2)
        self.list_with_data.delete(3)
        self.assertEqual(self.list_with_data.len(), 2)
        self.assertEqual(self.list_with_data.head.value, 1)
        self.assertEqual(self.list_with_data.tail.value, 2)
        self.assertIsNone(self.list_with_data.tail.next)

    def test_clean_empty(self):
        self.empty_list.clean()
        self.assertEqual(self.empty_list.len(), 0)
        self.assertIsNone(self.empty_list.head)
        self.assertIsNone(self.empty_list.tail)


    def test_clean_one_element_list(self):
        self.list_with_one_element.clean()
        self.assertEqual(self.list_with_one_element.len(), 0)
        self.assertIsNone(self.list_with_one_element.head)
        self.assertIsNone(self.list_with_one_element.tail)

    def test_clean(self):
        self.list_with_data.clean()
        self.assertEqual(self.list_with_data.len(), 0)
        self.assertIsNone(self.list_with_data.head)
        self.assertIsNone(self.list_with_data.tail)

    def test_len(self):
        self.assertEqual(self.list_with_data.len(), 5)
        self.assertEqual(self.empty_list.len(), 0)
        self.assertEqual(self.list_with_one_element.len(), 1)

    def test_insert(self):
        n1 = Node(2)
        self.list_with_data.insert(None, n1)
        self.assertEqual(self.list_with_data.len(), 6)
        self.assertEqual(self.list_with_data.head, n1)
        n2 = Node(10)
        self.list_with_data.insert(self.list_with_data.tail, n2)
        self.assertEqual(self.list_with_data.len(), 7)
        self.assertEqual(self.list_with_data.tail, n2)
        self.assertIsNone(self.list_with_data.tail.next)
        n3 = Node(15)
        afterNode = self.list_with_data.find(1)
        self.list_with_data.insert(afterNode=afterNode, newNode=n3)
        self.assertEqual(self.list_with_data.len(), 8)
        inserted_node = self.list_with_data.find(n3.value)
        self.assertEqual(inserted_node, n3)
        self.assertEqual(inserted_node.next.value, 2)



    def test_add_before_head(self):
        n1 = Node(2)
        self.list_with_one_element.add_before_head(n1)
        self.assertEqual(self.list_with_one_element.len(), 2)
        self.assertEqual(self.list_with_one_element.head, n1)
        self.assertEqual(self.list_with_one_element.head.next, self.list_with_one_element.tail)

    def test_add_before_head_empty_list(self):
        n1 = Node(2)
        self.empty_list.add_before_head(n1)
        self.assertEqual(self.empty_list.len(), 1)
        self.assertEqual(self.empty_list.head, n1)
        self.assertEqual(self.empty_list.tail, n1)
        self.assertIsNone(self.empty_list.head.next)
        self.assertIsNone(self.empty_list.tail.next)



    def test_insert_empty_list(self):
        self.empty_list.insert(None, newNode=Node(1))
        self.assertEqual(self.empty_list.head.value, 1)
        self.assertEqual(self.empty_list.tail.value, 1)
        self.assertIsNone(self.empty_list.tail.next)
        self.assertEqual(self.empty_list.len(), 1)
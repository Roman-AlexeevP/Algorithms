from unittest import TestCase

from OrderedList import OrderedList, Node, OrderedStringList


class TestOrderedList(TestCase):

    def setUp(self) -> None:
        self.asc_list = OrderedList(asc=True)
        self.desc_list = OrderedList(asc=False)

    def test_add_asc(self):
        self.asc_list.add(15)
        self.asc_list.add(5)
        self.asc_list.add(35)
        self.assertEqual(self.asc_list.len(), 3)
        self.assertIsNotNone(self.asc_list.head)
        self.assertIsNotNone(self.asc_list.tail)
        values = list(map(lambda x: x.value, self.asc_list.get_all()))
        self.assertEqual(values, [5, 15, 35])

    def test_add_desc(self):
        self.desc_list.add(15)
        self.desc_list.add(5)
        self.desc_list.add(35)
        self.assertEqual(self.desc_list.len(), 3)
        self.assertIsNotNone(self.desc_list.head)
        self.assertIsNotNone(self.desc_list.tail)
        values = list(map(lambda x: x.value, self.desc_list.get_all()))
        self.assertEqual(values, [35, 15, 5])

    def test_find_desc_none(self):
        self.desc_list.add(10)
        self.desc_list.add(15)
        self.desc_list.add(20)
        self.assertIsNone(self.desc_list.find(16))

    def test_find_desc_tail(self):
        self.desc_list.add(12)
        self.desc_list.add(10)
        self.desc_list.add(267)

        self.assertEqual(self.desc_list.find(267), self.desc_list.head)
        self.assertEqual(self.desc_list.find(10), self.desc_list.tail)
        self.assertIsNotNone(self.desc_list.find(12))

    def test_add_one(self):
        self.desc_list.add(5)
        self.asc_list.add(5)

        self.assertIsNotNone(self.desc_list.head)
        self.assertIsNotNone(self.asc_list.head)
        self.assertEqual(self.asc_list.len(), 1)
        self.assertEqual(self.desc_list.len(), 1)
        self.assertIsNotNone(self.desc_list.tail)
        self.assertIsNotNone(self.asc_list.tail)

    def test_delete(self):
        self.asc_list.add(5)
        self.asc_list.add(10)
        self.asc_list.add(15)

        self.asc_list.delete(10)

        self.assertEqual(self.asc_list.len(), 2)
        self.assertEqual(self.asc_list.head.value, 5)
        self.assertEqual(self.asc_list.tail.value, 15)

        self.asc_list.delete(5)

        self.assertEqual(self.asc_list.len(), 1)
        self.assertEqual(self.asc_list.head.value, 15)
        self.assertEqual(self.asc_list.tail.value, 15)
        self.assertEqual(self.asc_list.tail, self.asc_list.head)


class TestOrderedStringList(TestCase):


    def test_string_list_asc(self):
        lst = OrderedStringList(asc=True)

        lst.add(" b ")
        lst.add(" c")
        lst.add("a")

        values = list(map(lambda x: x.value, lst.get_all()))
        self.assertEqual(lst.len(), 3)
        self.assertEqual(values, ['a', ' b ', ' c'])
        self.assertIsNotNone(lst.head)
        self.assertIsNotNone(lst.tail)


    def test_string_list_desc(self):
        desc_lst = OrderedStringList(asc=False)

        desc_lst.add("faf")
        desc_lst.add("bar")
        desc_lst.add("python")

        values = list(map(lambda x: x.value, desc_lst.get_all()))
        self.assertEqual(desc_lst.len(), 3)
        self.assertEqual(values, ['python', 'faf', 'bar'])
        self.assertIsNotNone(desc_lst.head)
        self.assertIsNotNone(desc_lst.tail)
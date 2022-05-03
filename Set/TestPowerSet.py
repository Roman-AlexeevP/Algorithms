import string
import random
from unittest import TestCase

from PowerSet import PowerSet

def random_string(n):
    return ''.join(random.choices(string.ascii_letters, k=n))

class TestPowerSet(TestCase):

    def setUp(self) -> None:
        self.my_set = PowerSet()
        self.strings = [random_string(5) for i in range(20000)]

    def test_put(self):

        for val in self.strings:
            self.my_set.put(val)
        for val in self.strings:
            self.assertIn(val, self.my_set.items.values())

    def test_same_put(self):
        self.my_set.put("foo")
        self.my_set.put("foo")
        self.assertEqual(self.my_set.size(), 1)


    def test_get(self):
        self.my_set.put("foo")
        for val in self.strings:
            self.my_set.put(val)
        self.assertTrue(self.my_set.get("foo"))
        self.assertFalse(self.my_set.get(12345678))

    def test_intersection_empty(self):
        set_1 = PowerSet()
        set_2 = PowerSet()
        values_1 = ["foo", "bar", "lambda"]
        values_2 = ["bar", "lambda", "brain"]
        for i in range(3):
            set_1.put(values_1[i])
            set_2.put(values_2[i])
        set_inter = set_1.intersection(set_2)
        self.assertEqual(set_inter.size(), 2)
        self.assertIn("lambda", set_inter.items.values())
        self.assertIn("bar", set_inter.items.values())

    def test_empty_intersection(self):
        set_1 = PowerSet()
        set_2 = PowerSet()
        values_1 = ["foo", "bar", "lambda"]
        values_2 = ["brain", "lala", "baba"]
        set_3 = PowerSet()
        for i in range(3):
            set_1.put(values_1[i])
            set_2.put(values_2[i])
        set_inter = set_1.intersection(set_2)
        self.assertEqual(set_inter.size(), 0)
        set_inter = set_inter.intersection(set_3)
        self.assertEqual(set_inter.size(), 0)

    def test_union_sm(self):
        set1 = PowerSet()
        set2 =PowerSet()
        vals1 = [i for i in range(1, 10)]
        vals2 = [i for i in range(5, 15)]
        for val in vals1:
            set1.put(val)
        for val in vals2:
            set2.put(val)
        result = set1.union(set2)
        self.assertEqual(result.size(), 14)
        self.assertEqual([i for i in range(1,15)], list(result.items.values()))

    def test_union_empty(self):
        self.my_set.put("foo")
        self.my_set.put("bar")
        empty = PowerSet()
        res = self.my_set.union(empty)
        self.assertEqual(res.size(), 2)
        self.assertIn("foo", self.my_set.items.values())
        self.assertIn("bar", self.my_set.items.values())

    def test_union(self):
        values_1 = [random_string(3) for i in range(10000)]
        values_2 = [random_string(3) for i in range(10000)]
        set1 = PowerSet()
        set2 = PowerSet()
        for i in range(10000):
            set1.put(values_1[i])
            set2.put(values_2[i])

        self.assertIsNotNone(set1.union(set2))

    def test_diff(self):
        set1 = PowerSet()
        set2 = PowerSet()
        vals1 = [i for i in range(1, 10)]
        vals2 = [i for i in range(5, 15)]
        for val in vals1:
            set1.put(val)
        for val in vals2:
            set2.put(val)
        result = set1.difference(set2)
        self.assertEqual(result.size(), 4)
        self.assertEqual([i for i in range(1, 5)], list(result.items.values()))

    def test_diff_empty(self):
        set1 = PowerSet()
        set2 = PowerSet()
        for i in range(5):
            set1.put(i)
            set2.put(i)

        res = set1.difference(set2)
        self.assertEqual(res.size(), 0)

    def test_subset(self):
        set1 = PowerSet()
        for i in range(5):
            set1.put(i)
        set2 = PowerSet()
        self.assertFalse(set1.issubset(set2))
        for i in range(7):
            set2.put(i)

        self.assertFalse(set1.issubset(set2))\

    def test_subset_true(self):
        set1 = PowerSet()
        for i in range(5):
            set1.put(i)
        set2 = PowerSet()
        for i in range(5):
            set2.put(i)
        self.assertTrue(set1.issubset(set2))

    def test_intersection_empty_param(self):
        self.my_set.put("foo")
        set2 = PowerSet()
        res = self.my_set.intersection(set2)
        self.assertEqual(res.size(), 0)
        self.assertEqual(len(res.items), 0)
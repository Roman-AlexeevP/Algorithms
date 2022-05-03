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


    def test_union_sm(self):
        set1 = PowerSet()
        set2 = PowerSet()
        vals1 = [i for i in range(1, 10)]
        vals2 = [i for i in range(5, 15)]
        for val in vals1:
            set1.put(val)
        for val in vals2:
            set2.put(val)
        result = set1.union(set2)
        self.assertEqual(result.size(), 14)
        self.assertEqual([i for i in range(1, 15)], list(result.items.values()))

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
        union = set1.union(set2)
        self.assertTrue(isinstance(union, PowerSet))
        self.assertIsNotNone(union)

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
        self.assertTrue(isinstance(result, PowerSet))
        self.assertEqual(result.size(), 4)
        self.assertEqual([i for i in range(1, 5)], list(result.items.values()))

    def test_diff_empty(self):
        set1 = PowerSet()
        set2 = PowerSet()
        for i in range(5):
            set1.put(i)
            set2.put(i)

        res = set1.difference(set2)
        self.assertTrue(isinstance(res, PowerSet))
        self.assertEqual(res.size(), 0)

    def test_subset(self):
        set1 = PowerSet()
        for i in range(5):
            set1.put(i)
        set2 = PowerSet()
        self.assertTrue(set1.issubset(set2))
        for i in range(7):
            set2.put(i)

        self.assertFalse(set1.issubset(set2))

    def test_remove(self):
        self.my_set.put("foo")
        self.assertTrue(self.my_set.remove("foo"))
        self.assertEqual(self.my_set.size(), 0)
        self.assertFalse(self.my_set.remove("bar"))

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
        self.assertTrue(isinstance(res, PowerSet))
        self.assertEqual(res.size(), 0)
        self.assertEqual(len(res.items), 0)

    def test_union_sets(self):
        main_set = PowerSet()
        for i in range(0, 5):
            main_set.put(i)
        self.assertEqual(main_set.size(), 5)

        empty_set = PowerSet()

        union_set = main_set.union(empty_set)
        self.assertTrue(isinstance(union_set, PowerSet))
        self.assertEqual(union_set.size(), 5)
        for i in range(0, 5):
            self.assertIn(i, union_set.items)

    def test_union_empty_with_empty(self):
        main_set = PowerSet()

        empty_set = PowerSet()

        union_set = main_set.union(empty_set)
        self.assertTrue(isinstance(union_set, PowerSet))
        self.assertEqual(union_set.size(), 0)

    def test_union_non_empty(self):
        main_set = PowerSet()

        additional_set = PowerSet()
        additional_set.put("foo")
        additional_set.put("aoa")

        result = main_set.union(additional_set)
        self.assertTrue(isinstance(result, PowerSet))
        self.assertEqual(result.size(), 2)
        self.assertIn("foo", result.items)
        self.assertIn("aoa", result.items)

    def test_difference_two(self):
        first_set = PowerSet()
        second_set = PowerSet()
        result = first_set.difference(second_set)
        self.assertTrue(isinstance(result, PowerSet))
        self.assertEqual(result.size(), 0)
        first_set.put("foo")
        second_set.put("bar")
        result = first_set.difference(second_set)
        self.assertTrue(isinstance(result, PowerSet))
        self.assertEqual(result.size(), 1)
        self.assertIn("foo", result.items)

    def test_intersection_non_empty(self):
        first_set = PowerSet()
        second_set = PowerSet()

        test_values = ["foo", "bar", "test"]
        test_values_second = ["bar", "test", "lambda"]
        result_values = ["bar", "test"]

        for i in range(3):
            first_set.put(test_values[i])
            second_set.put(test_values_second[i])

        result = first_set.intersection(second_set)
        self.assertTrue(isinstance(result, PowerSet))
        self.assertEqual(result.size(), 2)
        for value in result_values:
            self.assertIn(value, result.items)

    def test_intersection_empty(self):
        first_set = PowerSet()
        second_set = PowerSet()

        first_set.put("foo")

        result = first_set.intersection(second_set)
        self.assertTrue(isinstance(result, PowerSet))
        self.assertEqual(result.size(), 0)

    def test_subsets(self):
        first_set = PowerSet()
        second_set = PowerSet()
        self.assertTrue(first_set.issubset(second_set))
        self.assertTrue(second_set.issubset(first_set))
        test_values = ["foo", "bar", "test"]
        for value in test_values:
            first_set.put(value)
        self.assertTrue(first_set.issubset(second_set))
        self.assertFalse(second_set.issubset(first_set))

        for value in test_values:
            second_set.put(value)

        self.assertTrue(first_set.issubset(second_set))
        self.assertTrue(second_set.issubset(first_set))

    def test_issubset_second(self):
        first_set = PowerSet()
        second_set = PowerSet()
        test_values = ["foo", "bar", "test"]
        test_values_second = ["foo", "bar", "test", "lambda", "skyrim"]
        for value in test_values:
            first_set.put(value)
        for value in test_values_second:
            second_set.put(value)

        self.assertTrue(second_set.issubset(first_set))
        self.assertFalse(first_set.issubset(second_set))

    def test_issubset_third(self):
        first_set = PowerSet()
        second_set = PowerSet()
        test_values = ["foo", "bar", "test", "oblivion"]
        test_values_second = ["foo", "bar", "test", "lambda", "skyrim"]
        for value in test_values:
            first_set.put(value)
        for value in test_values_second:
            second_set.put(value)

        self.assertFalse(second_set.issubset(first_set))
        self.assertFalse(first_set.issubset(second_set))

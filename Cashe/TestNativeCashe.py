from unittest import TestCase

from NativeCashe import NativeCashe

class TestNativeCashe(TestCase):

    def setUp(self) -> None:
        self.cashe = NativeCashe(sz=10)

    def test_find_min_hits(self):
        for i in range(10):
            self.cashe.put(str(i), f"foo #{i}")
        for i in range(100):
            if i != 1:
                self.cashe.get(str(i))
        min_index = self.cashe.hash_fun(str(1))
        self.assertEqual(self.cashe.find_min_hits(), min_index)

        self.cashe.remove_by_hits()
        self.assertIsNone(self.cashe.slots[min_index])
        self.assertIsNone(self.cashe.values[min_index])
        self.assertEqual(self.cashe.hits[min_index], 0)

    def test_get(self):
        self.cashe.put("foo", 1)
        self.cashe.put("bar", 2)
        self.assertEqual(self.cashe.get("foo"), 1)
        self.assertEqual(self.cashe.get("bar"), 2)
        self.assertEqual(self.cashe.hits[self.cashe.hash_fun("foo")], 1)
        self.assertEqual(self.cashe.hits[self.cashe.hash_fun("bar")], 1)


    def test_put(self):
        for i in range(10):
            self.cashe.put(str(i), f"foo #{i}")
        key, value = "foo", "bar"
        self.assertIsNotNone(self.cashe.put(key, value))

        self.assertIn(value, self.cashe.values)
        self.assertIn(key, self.cashe.slots)
        self.assertEqual(self.cashe.hits[self.cashe.hash_fun(key)], 0)

    def test_remove_by_hits(self):
        for i in range(10):
            self.cashe.put(str(i), f"foo #{i}")
        for i in range(10):
            if i != 0:
                self.cashe.get(str(i))
                key, value = "foooo", "baaar"
        min_index = self.cashe.hits.index(min(self.cashe.hits))

        self.assertEqual(self.cashe.put(key, value), min_index)
        self.assertIn(key, self.cashe.slots)
        self.assertIn(value, self.cashe.values)

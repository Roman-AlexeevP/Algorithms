import random
import string
from unittest import TestCase

from HashTable import HashTable

def random_string(n):
    return ''.join(random.choices(string.ascii_letters, k=n))

class TestQueue(TestCase):
    def setUp(self) -> None:
        self.hashtable = HashTable(sz=7, stp=1)

    def test_hash_fun(self):
        values = [random_string(i) for i in range(1,1000)]
        self.assertTrue(all(self.hashtable.hash_fun(val) < self.hashtable.size for val in values))

    def test_seek_slot(self):

        for i in range(6):
            self.hashtable.slots[i] = "foo"
        self.assertEqual(self.hashtable.seek_slot("foo"), 6)
        self.hashtable.slots[6] = "foo"
        self.assertIsNone(self.hashtable.seek_slot("foo"))

    def test_put(self):
        self.assertIsNotNone(self.hashtable.put("foo"))
        self.assertTrue("foo" in self.hashtable.slots)

    def test_put_none(self):
        for i in range(self.hashtable.size):
            self.assertIsNotNone(self.hashtable.put("foo"))
        self.assertIsNone(self.hashtable.put("bar"))

    def test_random_put(self):
        values = [random_string(i) for i in range(3,18)]
        random_hashtable = HashTable(sz=19, stp=3)
        for v in values:
            self.assertIsNotNone(random_hashtable.put(v))
        self.assertTrue(all([value in random_hashtable.slots for value in values]))

    def test_empty_put(self):
        hashtable_empty = HashTable(sz=0, stp=7)
        self.assertIsNone(hashtable_empty.put("fff"))
        self.assertIsNone(hashtable_empty.find("fff"))
        self.assertEqual(hashtable_empty.slots, [])

    def test_find(self):
        s1 = "foo"
        s2 = "bartr"
        s3 = "aoa"
        s4 = "aoaa"
        self.hashtable.put(s1)
        self.hashtable.put(s2)
        self.hashtable.put(s3)

        self.assertEqual(self.hashtable.slots[self.hashtable.find(s1)], s1)
        self.assertEqual(self.hashtable.slots[self.hashtable.find(s2)], s2)
        self.assertEqual(self.hashtable.slots[self.hashtable.find(s3)], s3)
        self.assertIsNone(self.hashtable.find(s4))
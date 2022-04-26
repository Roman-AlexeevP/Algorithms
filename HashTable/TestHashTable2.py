import random
import string
from unittest import TestCase

from HashTable2 import HashTable2

def random_string(n):
    return ''.join(random.choices(string.ascii_letters, k=n))

class TestQueue(TestCase):
    def setUp(self) -> None:
        self.hashtable = HashTable2(sz=19, stp=3)

    def test_hash_fun(self):
        values = [random_string(i) for i in range(1,1000)]
        self.assertTrue(all(self.hashtable.hash_fun(val) < self.hashtable.size for val in values))

    def test_hash_step(self):
        s = "foo"
        hsh = self.hashtable.hash_fun(s)
        for i in range(20):
            print(hsh)
            hsh = (hsh + 3) % 19

    def test_hash_fun_second(self):
        values = [random_string(i) for i in range(1,1000)]
        self.assertTrue(all(self.hashtable.hash_fun_second(val) < self.hashtable.size for val in values))

    def test_seek_slot(self):
        s1 = "foo"
        s2 = "aoa"
        s3 = "bbm"
        self.hashtable.put(s1)
        self.hashtable.put(s2)
        self.hashtable.put(s3)

        self.assertIn(s1, self.hashtable.slots),
        self.assertIn(s2, self.hashtable.slots)
        self.assertIn(s3, self.hashtable.slots)

    def test_find(self):
        s1 = "foo"
        s2 = "aoa"
        s3 = "bbm"
        self.hashtable.put(s1)
        self.hashtable.put(s2)
        self.hashtable.put(s3)
        print(self.hashtable.slots)
        self.assertIsNotNone(self.hashtable.find(s1))
        self.assertIsNotNone(self.hashtable.find(s2))
        self.assertIsNotNone(self.hashtable.find(s3))
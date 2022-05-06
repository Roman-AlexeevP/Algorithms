import random
import string
from unittest import TestCase
from collections import deque
from BloomFIlter import BloomFilter

def random_string(n):
    return ''.join(random.choices(string.ascii_letters, k=n))


class TestBloomFilter(TestCase):

    def setUp(self) -> None:
        self.filter = BloomFilter(32)

    def test_hash1(self):
        strings = [random_string(9) for i in range(100)]
        hashes = [self.filter.hash1(rand_string) for rand_string in strings]
        self.assertEqual(len(list(filter(lambda x: x>32, hashes))), 0)

    def test_hash2(self):
        strings = [random_string(9) for i in range(100)]
        hashes = [self.filter.hash2(rand_string) for rand_string in strings]
        self.assertEqual(len(list(filter(lambda x: x > 32, hashes))), 0)


    def test_is_value_list(self):
        digits = deque("0123456789")
        for i in range(10):
            self.filter.add(''.join(digits))
            digits.rotate(-1)
        for i in range(10):
            self.assertTrue(self.filter.is_value(''.join(digits)))
            digits.rotate(-1)

    def test_is_value(self):
        value = "foo"
        self.filter.add(value)
        self.assertTrue(self.filter.is_value(value))
        self.assertFalse(self.filter.is_value("vaar"))

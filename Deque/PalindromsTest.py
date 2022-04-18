from unittest import TestCase
from palindroms import is_palindrom

class Test(TestCase):

    def test_is_palindrom(self):
        self.assertTrue(is_palindrom("abba"))
        self.assertTrue(is_palindrom("aba"))
        self.assertTrue(is_palindrom("a"))
        self.assertTrue(is_palindrom("aa"))
        self.assertTrue(is_palindrom("babab"))
        self.assertTrue(is_palindrom("tacocat"))

    def test_is_palindrom_wrong(self):
        self.assertFalse(is_palindrom("acs"))
        self.assertFalse(is_palindrom("acda"))
        self.assertFalse(is_palindrom("foobar"))
        self.assertFalse(is_palindrom("Jojaro"))
        self.assertFalse(is_palindrom("Icigo CUrosaki"))
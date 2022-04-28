from unittest import TestCase

from Dictionary.NativeDictionary import NativeDictionary


class TestDictionary(TestCase):

    def setUp(self) -> None:
        self.dictionary = NativeDictionary(sz=19)

    def test_put(self):

        self.assertIsNotNone(self.dictionary.put("key", "value"))
        self.assertIn("key", self.dictionary.slots)
        self.assertIn("value", self.dictionary.values)

    def test_put_exist(self):
        self.assertIsNotNone(self.dictionary.put("key", "value"))
        self.assertIsNotNone(self.dictionary.put("key", "value2"))
        self.assertIn("key", self.dictionary.slots)
        self.assertEqual(self.dictionary.slots.count("key"), 1)
        self.assertIn("value2", self.dictionary.values)
        self.assertNotIn("value", self.dictionary.values)

    def test_get(self):
        self.dictionary.slots[0] = "foo"
        self.dictionary.values[0] = "bar"
        self.assertEqual(self.dictionary.get("foo"), "bar")
        self.assertIsNone(self.dictionary.get("empty_foo"))

    def test_is_key(self):
        self.dictionary.slots[0] = "foo"
        self.dictionary.values[0] = "bar"
        self.assertTrue(self.dictionary.is_key("foo"))
        self.assertFalse(self.dictionary.is_key("bar"))

    def test_put(self):
        self.dictionary.put("foo", "bar")
        self.assertEqual(self.dictionary.get("foo"), "bar")
        self.dictionary.put("bar", "foo")
        self.assertEqual(self.dictionary.get("bar"), "foo")
        self.dictionary.put("foo", "bar2")
        self.assertEqual(self.dictionary.get("foo"), "bar2")

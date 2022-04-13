from unittest import TestCase

from DynamicArray.DynArray import DynArray


class TestDynArray(TestCase):

    def setUp(self) -> None:
        self.array = DynArray()

    def test_insert_to_begin(self):
        self.array.append(10)
        self.array.append(20)
        self.array.insert(0, 30)
        self.assertEqual(self.array.count, 3)
        self.assertEqual(self.array.capacity, 16)
        self.assertEqual(self.array[0], 30)
        self.assertEqual(self.array[1], 10)
        self.assertEqual(self.array[2], 20)

    def test_insert_wrong_position(self):
        self.array.append('foo')
        with self.assertRaises(IndexError):
            self.array.insert(2, 'bar')

    def test_insert_with_resize(self):
        for i in range(1, 17):
            # [1..16]
            self.array.append(i)
        self.array.insert(14, 'foo')
        self.assertEqual(self.array.count, 17)
        self.assertEqual(self.array.capacity, 32)
        self.assertEqual(self.array[14], 'foo')
        self.assertEqual(self.array[15], 15)
        self.assertEqual(self.array[16], 16)

    def test_insert_without_resize(self):
        for i in range(1, 6):
            self.array.append(i)

        self.array.insert(1, 'foo')
        for itm in self.array:
            print(itm)
        self.assertEqual(self.array.count, 6)
        self.assertEqual(self.array.capacity, 16)
        self.assertEqual(self.array[1], 'foo')
        self.assertEqual(self.array[2], 2)
        self.assertEqual(self.array[5], 5)

    def test_delete_wrong_position(self):
        self.array.append('foo')
        with self.assertRaises(IndexError):
            self.array.delete(2)

    def test_delete_one_element(self):
        self.array.append('foo')
        self.array.delete(0)
        self.assertEqual(self.array.capacity, 16)
        self.assertEqual(self.array.count, 0)

    def test_delete_from_center(self):
        for i in range(1, 4):  # [1,2,3]
            self.array.append(i)
        self.array.delete(1)
        self.assertEqual(self.array.count, 2)
        self.assertEqual(self.array.capacity, 16)
        self.assertEqual(self.array[0], 1)
        self.assertEqual(self.array[1], 3)

    def test_delete_from_center_resized(self):
        for i in range(1, 18):  # [1..17]
            self.array.append(i)
        self.assertEqual(self.array.capacity, 32)
        self.assertEqual(self.array.count, 17)
        self.array.delete(16)
        self.assertEqual(self.array.count, 16)
        self.assertEqual(self.array.capacity, 21)
        for _ in range(6):
            self.array.delete(1)
        self.assertEqual(self.array.count, 10)
        self.assertEqual(self.array.capacity, 16)

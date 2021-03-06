from unittest import TestCase

from Stack import is_balanced_string, Stack
from postfix_calculation import calcucate_postfix


class Test(TestCase):
    def test_is_balanced_string_right(self):
        self.assertTrue(is_balanced_string("()"))

    def test_is_balanced_string_right_2(self):
        self.assertTrue(is_balanced_string("()()()((()()))"))

    def test_is_balanced_string_right_3(self):
        self.assertTrue(is_balanced_string("()()()((()()))"))

    def test_is_balanced_string_right_4(self):
        self.assertTrue(is_balanced_string("(()()()())"))

    def test_is_balanced_string_wrong(self):
        self.assertFalse(is_balanced_string("())("))

    def test_is_balanced_string_wrong_2(self):
        self.assertFalse(is_balanced_string("))(("))

    def test_is_balanced_string_wrong_3(self):
        self.assertFalse(is_balanced_string("((())"))


class StackTest(TestCase):

    def setUp(self) -> None:
        self.stack = Stack()

    def test_push(self):
        for i in range(10):
            self.stack.push(i)
        self.assertEqual(self.stack.size(), 10)
        for i in range(10):
            self.assertEqual(self.stack.stack[i], i)

    def test_pop_empty(self):
        self.assertIsNone(self.stack.pop())

    def test_pop_one(self):
        self.stack.push(12)
        self.assertEqual(self.stack.pop(), 12)
        self.assertEqual(self.stack.size(), 0)

    def test_peek(self):
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)
        self.assertEqual(self.stack.size(), 1)

class PostfixCalculateTest(TestCase):

    def test_calculation(self):
        stack = Stack()
        stack.push("=")
        stack.push("*")
        stack.push(3)
        stack.push("+")
        stack.push(2)
        stack.push(1)
        value = calcucate_postfix(stack)
        self.assertEqual(value, 9)


    def test_calculation_2(self):
        expression = "82+5*9+="
        stack = Stack()
        stack.push("=")
        stack.push('+')
        stack.push(9)
        stack.push("*")
        stack.push(5)
        stack.push("+")
        stack.push(8)
        stack.push(2)
        value = calcucate_postfix(stack)
        self.assertEqual(value, 59)

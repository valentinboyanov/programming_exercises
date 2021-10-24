import unittest
from typing import List

# 15. Write functions that add, subtract, and multiply two numbers in
# their digit-list representation (and return a new digit list).
# If you’re ambitious you can implement Karatsuba multiplication.
# Try different bases. What is the best base if you care about speed?
# If you couldn’t completely solve the prime number exercise above
# due to the lack of large numbers in your language, you can now use
# your own library for this task.


def add(a: List[int], b: List[int]) -> List[int]:
    number_a = to_int(a)
    number_b = to_int(b)

    return to_list(number_a + number_b)


def substract(a: List[int], b: List[int]) -> List[int]:
    number_a = to_int(a)
    number_b = to_int(b)

    return to_list(number_a - number_b)


def multiply(a: List[int], b: List[int]) -> List[int]:
    number_a = to_int(a)
    number_b = to_int(b)

    return to_list(number_a * number_b)


def to_int(digits: List[int]) -> int:
    text_digits = [str(n) for n in digits]
    text = "".join(text_digits)

    return int(text)


def to_list(number: int) -> List[int]:
    digits: List[int] = []
    text = str(number)

    for character in text:
        digits.append(int(character))

    return digits


class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual([2, 2, 2], add([1, 1, 1], [1, 1, 1]))
        self.assertEqual([1, 1, 3], add([1, 1, 1], [2]))

    def test_substract(self):
        self.assertEqual([1, 1, 1], substract([2, 2, 2], [1, 1, 1]))
        self.assertEqual([1, 1, 0], substract([1, 1, 1], [1]))

    def test_multiply(self):
        self.assertEqual([1, 0, 0], multiply([1, 0], [1, 0]))
        self.assertEqual([3, 6], multiply([1, 2], [3]))

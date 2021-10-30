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


def karatsuba_multiply(a: List[int], b: List[int]) -> List[int]:
    base = 10
    m = 2
    n = min(len(a), len(b))

    if n > m:
        a1 = to_int(a[:-m])
        a0 = to_int(a[-m:])

        b1 = to_int(b[:-m])
        b0 = to_int(b[-m:])

        z2 = a1 * b1
        z1 = (a1 * b0) + (a0 * b1)
        z0 = a0 * b0

        result = z2 * (base ** (2 * m)) + z1 * (base ** m) + z0

        return to_list(result)
    else:
        return to_list(to_int(a) * to_int(b))


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

    def test_karatsuba_multiply(self):
        self.assertEqual([1, 0, 0], karatsuba_multiply([1, 0], [1, 0]))
        self.assertEqual([3, 6], karatsuba_multiply([1, 2], [3]))
        self.assertEqual([5, 6, 0, 8, 8], karatsuba_multiply([1, 2, 3], [4, 5, 6]))
        self.assertEqual(
            [7, 0, 0, 6, 6, 5, 2], karatsuba_multiply([1, 2, 3, 4], [5, 6, 7, 8])
        )

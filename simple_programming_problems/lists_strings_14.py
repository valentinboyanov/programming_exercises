import unittest
from typing import List

# 14. Write a function that takes a number and returns a list of its digits.
# So for 2342 it should return [2,3,4,2].


def to_list(number: int) -> List[int]:
    digits: List[int] = []
    text = str(number)

    for character in text:
        digits.append(int(character))

    return digits


class Test(unittest.TestCase):
    def test_int_to_list(self):
        self.assertEqual([2, 3, 4, 2], to_list(2342))

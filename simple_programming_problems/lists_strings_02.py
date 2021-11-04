import unittest
from typing import Any, List

# 2. Write function that reverses a list, preferably in place.


def reversed(elements: List[Any]) -> List[Any]:
    elements.reverse()

    return elements


class ReversedTest(unittest.TestCase):
    def test_different_elements(self):
        elements: List = [1, 2, 3]
        self.assertEqual([3, 2, 1], reversed(elements))

    def test_same_elements(self):
        elements: List = [1, 1, 1]
        self.assertEqual([1, 1, 1], reversed(elements))

    def test_empty_list(self):
        elements: List = []
        self.assertEqual([], reversed(elements))

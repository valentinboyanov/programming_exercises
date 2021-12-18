import unittest
from typing import Any, List

# 3. Write a function that checks whether an element occurs in a list.


def in_list(element: Any, elements: List) -> bool:
    return element in elements


class InListTest(unittest.TestCase):
    def test_in_list(self):
        self.assertTrue(in_list(1, [1, 2, 3]))
        self.assertFalse(in_list(4, [1, 2, 3]))

        self.assertTrue(in_list("a", ["a", "b", "c"]))
        self.assertFalse(in_list("d", ["a", "b", "c"]))

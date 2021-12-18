import unittest
from typing import List, Optional

# 1. Write a function that returns the largest element in a list.


def filter_largest_element(elements: List[int]) -> Optional[int]:
    largest_element: Optional[int] = None

    if len(elements) > 0:
        largest_element = elements[0]
        for e in elements:
            if e > largest_element:
                largest_element = e

    return largest_element


class FilterLargestElementTest(unittest.TestCase):
    def test_different_elements(self):
        elements = [3, 2, 5]
        largest_element = filter_largest_element(elements)
        self.assertEqual(5, largest_element)

    def test_same_elements(self):
        elements = [2, 2, 2]
        largest_element = filter_largest_element(elements)
        self.assertEqual(2, largest_element)

    def test_empty_list(self):
        elements: List[int] = []
        largest_element = filter_largest_element(elements)
        self.assertEqual(None, largest_element)

import unittest
from math import floor
from typing import List, Optional

# 18. Implement binary search.


def find_index(elements: List[int], target: int) -> Optional[int]:
    l: int = 0
    r: int = len(elements) - 1

    while l <= r:
        m = floor((l + r) / 2)
        if elements[m] < target:
            l = m + 1
        elif elements[m] > target:
            r = m - 1
        else:
            return m

    return None


class Test(unittest.TestCase):
    def test_binary_search(self):
        self.assertEqual(0, find_index([1, 3, 5, 8, 13, 21, 34, 55], 1))
        self.assertEqual(2, find_index([1, 3, 5, 8, 13, 21, 34, 55], 5))
        self.assertEqual(7, find_index([1, 3, 5, 8, 13, 21, 34, 55], 55))

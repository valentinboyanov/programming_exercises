import unittest
from typing import List

# 5. Write a function that computes the running total of a list.


def running_total(elements: List[int]) -> int:
    return sum(elements)


class RunningTotalTest(unittest.TestCase):
    def test_running_total(self):
        self.assertEqual(9, running_total([2, 3, 4]))

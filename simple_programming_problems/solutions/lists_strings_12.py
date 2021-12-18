import unittest
from collections import deque
from typing import Any, List

# Write a function that rotates a list by k elements.
# For example [1,2,3,4,5,6] rotated by two becomes [3,4,5,6,1,2].
# Try solving this without creating a copy of the list.
# How many swap or move operations do you need?


def rotate(elements: List[Any], k: int) -> List[Any]:
    elements.reverse()

    for _ in range(k):
        last = elements.pop()
        elements.insert(0, last)

    elements.reverse()

    return elements


def rotate_1(elements: List[Any], k: int) -> List[Any]:
    queue = deque(elements)

    for _ in range(k):
        first = queue.popleft()
        queue.append(first)

    return list(queue)


class RotateTest(unittest.TestCase):
    def test_rotate(self):
        self.assertEqual([3, 4, 5, 6, 1, 2], rotate([1, 2, 3, 4, 5, 6], 2))
        self.assertEqual([5, 6, 1, 2, 3, 4], rotate([1, 2, 3, 4, 5, 6], 4))


class Rotate1Test(unittest.TestCase):
    def test_rotate(self):
        self.assertEqual([3, 4, 5, 6, 1, 2], rotate_1([1, 2, 3, 4, 5, 6], 2))
        self.assertEqual([5, 6, 1, 2, 3, 4], rotate_1([1, 2, 3, 4, 5, 6], 4))

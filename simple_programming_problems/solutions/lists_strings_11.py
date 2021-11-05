import unittest
from typing import List, Optional

# 11. Write a function that merges two sorted lists into a new sorted list.
# [1,4,6],[2,3,5] → [1,2,3,4,5,6]. You can do this quicker than
# concatenating them followed by a sort.


def sorted_merge(a: List[int], b: List[int]) -> List[int]:
    merged_list: List[int] = []

    a.reverse()
    b.reverse()

    for _ in range(len(a) + len(b)):
        last_a = last_element(a)
        last_b = last_element(b)

        if last_a is None:
            merged_list.append(b.pop())
        elif last_b is None:
            merged_list.append(a.pop())
        else:
            if last_a < last_b:
                merged_list.append(a.pop())
            else:
                merged_list.append(b.pop())

    return merged_list


def last_element(elements: List[int]) -> Optional[int]:
    if len(elements) > 0:
        return elements[-1]
    else:
        return None


class Test(unittest.TestCase):
    def test_same_lenght(self):
        self.assertEqual([1, 2, 3, 4, 5, 6], sorted_merge([1, 4, 6], [2, 3, 5]))
        self.assertEqual([], sorted_merge([], []))

    def test_different_lenght(self):
        self.assertEqual([1, 2, 4, 6], sorted_merge([1, 4, 6], [2]))
        self.assertEqual([1, 4, 6], sorted_merge([1, 4, 6], []))

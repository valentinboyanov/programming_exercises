import unittest
from typing import List

# 17. Implement the following sorting algorithms: Selection sort,
# Insertion sort, Merge sort, Quick sort, Stooge Sort.
# Check Wikipedia for descriptions.


def selection_sort(elements: List[int]) -> List[int]:
    start_position = 0

    while start_position < len(elements):
        min_position = start_position
        min_value = elements[start_position:][0]

        for i in range(start_position, len(elements)):
            if elements[i] < min_value:
                min_position = i
                min_value = elements[i]

        del elements[min_position]
        elements.insert(start_position, min_value)

        start_position = start_position + 1

    return elements


def insertion_sort(elements: List[int]) -> List[int]:
    start_position = 1

    while start_position < len(elements):
        start_value = elements[start_position]

        last_position = 0
        should_move = False

        for i in range(start_position):
            if elements[i] > start_value:
                last_position = i
                should_move = True
                break

        if should_move == True:
            del elements[start_position]
            elements.insert(last_position, start_value)

        start_position = start_position + 1

    return elements


def merge_sort(elements: List[int]) -> List[int]:
    sublists: List[List[int]] = []

    for e in elements:
        sublists.append([e])

    while len(sublists) > 1:
        first = sublists.pop()
        second = sublists.pop()

        first.extend(second)
        first.sort()

        sublists.insert(0, first)

    return sublists[0]


def quick_sort(elements: List[int]) -> List[int]:

    return elements


class Test(unittest.TestCase):
    def test_selection_sort(self):
        self.assertEqual([1, 2, 3], selection_sort([2, 1, 3]))
        self.assertEqual([1, 2, 5, 6, 10], selection_sort([2, 5, 6, 10, 1]))
        self.assertEqual([1, 2, 5, 5, 6, 10], selection_sort([2, 5, 5, 6, 10, 1]))

    def test_insertion_sort(self):
        self.assertEqual([1, 2, 3], insertion_sort([2, 1, 3]))
        self.assertEqual([1, 2, 5, 6, 10], insertion_sort([2, 5, 6, 10, 1]))
        self.assertEqual([1, 2, 5, 5, 6, 10], insertion_sort([2, 5, 5, 6, 10, 1]))

    def test_merge_sort(self):
        self.assertEqual([1, 2, 3], merge_sort([2, 1, 3]))
        self.assertEqual([1, 2, 5, 6, 10], merge_sort([2, 5, 6, 10, 1]))
        self.assertEqual([1, 2, 5, 5, 6, 10], merge_sort([2, 5, 5, 6, 10, 1]))

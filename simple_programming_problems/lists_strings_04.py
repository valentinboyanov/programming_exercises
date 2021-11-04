import unittest
from typing import Any, Iterable, List

# 4. Write a function that returns the elements on odd positions in a list.


def filter_odd_positions(elements: List[Any]) -> List[Any]:
    odd_elements: List[Any] = []

    for n in range(0, len(elements)):
        if n % 2 != 0:
            odd_elements.append(elements[n])

    return odd_elements


def filter_odd_positions_2(elements: List[Any]) -> List[Any]:
    odd_elements: List[Any] = []

    for n in odd_numbers(start=0, stop=len(elements) - 1):
        odd_elements.append(elements[n])

    return odd_elements


def odd_numbers(start: int, stop: int) -> Iterable:
    for n in range(start, stop + 1):
        if n % 2 != 0:
            yield n


class FilterOddPositionsTest(unittest.TestCase):
    def test_empty_list(self):
        odd_positions = filter_odd_positions([])
        self.assertEqual(odd_positions, [])

    def test_one_element(self):
        odd_positions = filter_odd_positions(["a"])
        self.assertEqual(odd_positions, [])

    def test_odd_list(self):
        odd_positions = filter_odd_positions(["a", "b", "c", "d"])
        self.assertEqual(odd_positions, ["b", "d"])

    def test_even_list(self):
        odd_positions = filter_odd_positions(["a", "b", "c", "d", "e"])
        self.assertEqual(odd_positions, ["b", "d"])


class FilterOddPositions2Test(unittest.TestCase):
    def test_empty_list(self):
        odd_positions = filter_odd_positions_2([])
        self.assertEqual(odd_positions, [])

    def test_one_element(self):
        odd_positions = filter_odd_positions_2(["a"])
        self.assertEqual(odd_positions, [])

    def test_odd_list(self):
        odd_positions = filter_odd_positions_2(["a", "b", "c", "d"])
        self.assertEqual(odd_positions, ["b", "d"])

    def test_even_list(self):
        odd_positions = filter_odd_positions_2(["a", "b", "c", "d", "e"])
        self.assertEqual(odd_positions, ["b", "d"])

    def test_odd_numbers(self):
        odd_numbers_list: List[int] = [n for n in odd_numbers(0, 5)]
        self.assertEqual(odd_numbers_list, [1, 3, 5])

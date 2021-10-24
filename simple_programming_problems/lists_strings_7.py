import unittest
from typing import Any, List

# 7. Write three functions that compute the sum of the numbers in a list:
# using a for-loop, a while-loop and recursion. (Subject to availability
# of these constructs in your language of choice.)


def for_sum(elements: List[Any]) -> int:
    numbers: List[int] = to_int_list(elements)
    sum = 0

    for n in numbers:
        sum = sum + n

    return sum


def while_sum(elements: List[Any]) -> int:
    numbers: List[int] = to_int_list(elements)
    sum = 0

    last_position = len(numbers) - 1
    while last_position >= 0:
        sum = sum + numbers[last_position]
        last_position = last_position - 1

    return sum


def recursion_sum(elements: List[Any], sum: int = 0) -> int:
    numbers: List[int] = to_int_list(elements)

    if len(numbers) > 0:
        sum = sum + numbers.pop()
        return recursion_sum(numbers, sum)
    else:
        return sum


def to_int_list(elements: List[Any]) -> List[int]:
    numbers: List[int] = []

    for e in elements:
        if isinstance(e, int):
            numbers.append(e)

    return numbers


class Test(unittest.TestCase):
    def test_for_sum(self):
        self.assertEqual(9, for_sum([2, 3, "a", 4]))

    def test_while_sum(self):
        self.assertEqual(9, while_sum([2, 3, "a", 4]))

    def test_recursion_sum(self):
        self.assertEqual(9, recursion_sum([2, 3, "a", 4]))

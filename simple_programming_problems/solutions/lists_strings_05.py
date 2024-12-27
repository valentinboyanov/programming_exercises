# 5. Write a function that computes the running total of a list.

from typing import List


def running_total(elements: List[int]) -> int:
    """
    >>> running_total([2, 3, 4])
    9
    """
    return sum(elements)

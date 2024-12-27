# 5. Write a function that computes the running total of a list.

from typing import List, Tuple


def running_total(elements: List[int]) -> int:
    """
    >>> running_total([2, 3, 4])
    9
    """
    return sum(elements)


def calculate_running_total(elements: List[int]) -> List[int]:
    """
    >>> calculate_running_total([2, 3, 4, 5])
    [2, 5, 9, 14]
    >>> calculate_running_total([2, 3, 4, 5, 6, 7, 8])
    [2, 5, 9, 14, 20, 27, 35]
    """

    running_totals: List[int] = []

    for i, e in enumerate(elements):

        if i == 0:
            current_elements = [e]
            current_total = e
        else:
            (current_elements, current_total) = add_to_total(
                (current_elements, current_total), e
            )

        running_totals.append(current_total)

    return running_totals


def add_to_total(current_total: Tuple[List[int], int], n: int) -> Tuple[List[int], int]:
    """
    >>> add_to_total(([2, 3, 4], 9), 5)
    ([2, 3, 4, 5], 14)
    """
    (elements, sum) = current_total

    elements.append(n)
    sum += n

    new_total = (elements, sum)

    return new_total

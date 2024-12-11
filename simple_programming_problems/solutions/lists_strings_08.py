"""
8. Write a function on_all that applies a function to every element of a list.
Use it to print the first twenty perfect squares. The perfect squares can be
found by multiplying each natural number with itself. The first few perfect
squares are 1*1= 1, 2*2=4, 3*3=9, 4*4=16. Twelve for example is not a perfect
square because there is no natural number m so that m*m=12. (This question is
tricky if your programming language makes it difficult to pass functions as
arguments.)

>>> on_all([n for n in range(1, 20)], print_perfect_square)
1
4
9
16
25
36
49
64
81
100
121
144
169
196
225
256
289
324
361
"""

import doctest
from typing import Any, List


def on_all(elements: List[Any], func) -> None:
    """
    >>> on_all([1,2,3], print_perfect_square)
    1
    4
    9
    """
    for e in elements:
        func(e)


def print_perfect_square(number: int) -> None:
    """
    >>> print_perfect_square(3)
    9
    """
    square = number * number
    print(square)


if __name__ == "__main__":
    doctest.testmod()

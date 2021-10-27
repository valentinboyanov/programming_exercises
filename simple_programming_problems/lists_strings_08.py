import io
import unittest
from typing import Any, List
from unittest.mock import patch

# 8. Write a function on_all that applies a function to every element of a list.
# Use it to print the first twenty perfect squares. The perfect squares can be
# found by multiplying each natural number with itself. The first few perfect
# squares are 1*1= 1, 2*2=4, 3*3=9, 4*4=16. Twelve for example is not a perfect
# square because there is no natural number m so that m*m=12. (This question is
# tricky if your programming language makes it difficult to pass functions as
# arguments.)


def on_all(elements: List[Any], func) -> None:
    for e in elements:
        func(e)


def print_perfect_square(number: int) -> None:
    square = number * number
    print(square)


class Test(unittest.TestCase):
    def test_print_first_twenty_perfect_squares(self):
        twenty_numbers = [n for n in range(1, 20)]
        expected_output = """1
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

        with patch("sys.stdout", new_callable=io.StringIO) as mocked_output:
            on_all(twenty_numbers, print_perfect_square)
            self.assertEquals(expected_output, mocked_output.getvalue())


if __name__ == "__main__":
    twenty_numbers = [n for n in range(1, 20)]
    on_all(twenty_numbers, print_perfect_square)

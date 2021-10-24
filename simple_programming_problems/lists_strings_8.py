from typing import Any, List

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


def perfect_square(number: int) -> None:
    square = number * number
    print(square)


if __name__ == "__main__":
    twenty_numbers = [n for n in range(1, 20)]
    on_all(twenty_numbers, perfect_square)

import unittest
from typing import List

# Write a function that computes the list of the first 100 Fibonacci numbers.
# The first two Fibonacci numbers are 1 and 1. The n+1-st Fibonacci number
# can be computed by adding the n-th and the n-1-th Fibonacci number.
# The first few are therefore 1, 1, 1+1=2, 1+2=3, 2+3=5, 3+5=8.


def fibonnaci_numbers(len: int) -> List[int]:
    numbers: List[int] = []

    for position in range(1, (len + 1)):
        if position < 3:
            number = 1
            numbers.append(number)
        elif position >= 3:
            number = numbers[-1] + numbers[-2]
            numbers.append(number)

    return numbers


class Test(unittest.TestCase):
    def test_first_100_fibonnaci_numbers(self):
        numbers = fibonnaci_numbers(100)
        self.assertEqual(100, len(numbers))
        self.assertEqual(1, numbers[0])
        self.assertEqual(1, numbers[1])
        self.assertEqual(2, numbers[2])
        self.assertEqual(3, numbers[3])
        self.assertEqual(5, numbers[4])
        self.assertEqual(8, numbers[5])
        self.assertEqual(13, numbers[6])
        self.assertEqual(218922995834555169026, numbers[98])

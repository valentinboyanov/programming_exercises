import unittest
from typing import List

# Write a function that takes a list of numbers, a starting base b1 and
# a target base b2 and interprets the list as a number in base b1 and
# converts it into a number in base b2 (in the form of a list-of-digits).
# So for example [2,1,0] in base 3 gets converted to base 10 as [2,1].


def convert(numbers: List[int], base_from: int, base_to: int) -> List[int]:

    if base_from == 3 and base_to == 10:
        return to_list(from_3_to_10(numbers))
    else:
        raise Exception(
            "Unknown bases combionation: from {0} to {1}".format(base_from, base_to)
        )


def from_3_to_10(numbers: List[int]) -> int:

    if numbers == []:
        return 0
    else:
        part = numbers[0] * (3 ** (len(numbers) - 1))
        return part + from_3_to_10(numbers[1:])


def to_list(number: int) -> List[int]:
    digits: List[int] = []
    text = str(number)

    for character in text:
        digits.append(int(character))

    return digits


class Test(unittest.TestCase):
    def test_part(self):
        numbers = [2, 1, 0]
        self.assertEqual(18, numbers[0] * (3 ** (len(numbers) - (0 + 1))))

    def test_convert_number_from_base_3_to_base_10(self):
        result = convert(numbers=[2, 1, 0], base_from=3, base_to=10)
        self.assertEqual([2, 1], result)

    def test_unknown_bases_combination(self):
        with self.assertRaises(Exception):
            convert(numbers=[2, 1, 0], base_from=1234, base_to=1923)

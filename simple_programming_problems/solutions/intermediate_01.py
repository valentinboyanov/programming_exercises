import itertools
import unittest
from typing import List, NamedTuple, Set, Tuple

# Write a program that outputs all possibilities to put + or - or nothing
# between the numbers 1,2,…,9 (in this order) such that the result is 100.
# For example 1 + 2 + 3 - 4 + 5 + 6 + 78 + 9 = 100.


class NumbersCombination(NamedTuple):
    numbers: List[int]
    operations: List[str]


def get_operators() -> Set[Tuple]:
    possibilities = set()
    operators = ["+", "-", "nothing"]

    for p in itertools.product(operators, repeat=8):
        possibilities.add(p)

    return possibilities


def get_operations(operators: List[str], len: int) -> Set[Tuple]:
    operations = set()

    for p in itertools.product(operators, repeat=len):
        operations.add(p)

    return operations


def apply_nothing(combination: NumbersCombination) -> NumbersCombination:
    if "nothing" not in combination.operations:
        return combination
    else:
        i = combination.operations.index("nothing")
        n1 = combination.numbers[i]
        n2 = combination.numbers[i + 1]
        result = int("{0}{1}".format(str(n1), str(n2)))

        combination.numbers[i] = result
        del combination.numbers[i + 1]
        del combination.operations[i]

        return apply_nothing(
            NumbersCombination(
                numbers=combination.numbers, operations=combination.operations
            )
        )


def apply_operations(numbers: List[int], operations: List[str]) -> int:
    if "nothing" not in operations:
        for i in range(len(operations)):
            if operations[i] == "-":
                numbers[i + 1] = numbers[i + 1] * -1

        return sum(numbers)
    else:
        i = operations.index("nothing")
        n1 = numbers[i]
        n2 = numbers[i + 1]
        result = int("{0}{1}".format(str(n1), str(n2)))

        numbers[i] = result
        del numbers[i + 1]
        del operations[i]

        return apply_operations(numbers, operations)


def apply_sum(combination: NumbersCombination) -> int:
    for i in range(len(combination.operations)):
        if combination.operations[i] == "-":
            combination.numbers[i + 1] = combination.numbers[i + 1] * -1

    return sum(combination.numbers)


def get_result(combi: NumbersCombination) -> int:
    combi = apply_nothing(combi)

    return apply_sum(combi)


class Test(unittest.TestCase):
    def test_operators_possibilities(self):
        operators = get_operators()
        self.assertEqual(6561, len(operators))

    def test_apply_nothing(self):
        actual = NumbersCombination(
            numbers=[1, 2, 3, 4, 5], operations=["+", "nothing", "-", "nothing"]
        )
        expected = NumbersCombination(numbers=[1, 23, 45], operations=["+", "-"])
        self.assertEqual(expected, apply_nothing(actual))

    def test_apply_nothing_consecutive(self):
        actual = NumbersCombination(
            numbers=[1, 2, 3, 4, 5], operations=["+", "nothing", "nothing", "-"]
        )
        expected = NumbersCombination(numbers=[1, 234, 5], operations=["+", "-"])
        self.assertEqual(expected, apply_nothing(actual))

    def test_apply_sum_rest_operations(self):
        numbers = NumbersCombination(numbers=[1, 2, 3, 4], operations=["+", "+", "+"])
        self.assertEqual(10, apply_sum(numbers))

    def test_get_result(self):
        numbers = NumbersCombination(
            numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9],
            operations=["+", "+", "-", "+", "+", "+", "nothing", "+"],
        )
        self.assertEqual(100, get_result(numbers))


if __name__ == "__main__":
    operations = get_operations(operators=["+", "-", "nothing"], len=8)

    combinations: List[NumbersCombination] = []
    for o in operations:
        combinations.append(
            NumbersCombination(numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9], operations=list(o))
        )

    for c in combinations:
        if get_result(c) == 100:
            print(c.numbers)

import itertools
import unittest
from typing import List, Set, Tuple

# Write a program that outputs all possibilities to put + or - or nothing
# between the numbers 1,2,…,9 (in this order) such that the result is 100.
# For example 1 + 2 + 3 - 4 + 5 + 6 + 78 + 9 = 100.


def evaluate(expression: List[str]) -> int:
    if "nothing" in expression:
        i = expression.index("nothing")
        n1 = expression[i - 1]
        n2 = expression[i + 1]

        expression[i - 1] = "{0}{1}".format(n1, n2)
        del expression[i + 1]
        del expression[i]

        return evaluate(expression)

    elif "-" in expression:
        i = expression.index("-")
        n = expression[i + 1]

        expression[i + 1] = "-{0}".format(n)
        del expression[i]

        return evaluate(expression)

    elif "+" in expression:
        i = expression.index("+")

        del expression[i]

        return evaluate(expression)

    else:
        numbers = [int(element) for element in expression]

        return sum(numbers)


def make_expression(numbers: List[int], operations: List[str]) -> List[str]:
    expression: List[str] = []

    assert len(operations) == (len(numbers) - 1)

    for i in range(len(operations)):
        expression.append(str(numbers[i]))
        expression.append(operations[i])

    last_number = numbers[-1]
    expression.append(str(last_number))

    return expression


def ops_permutations(operations: List[str], len: int) -> Set[Tuple]:
    permutations = set()

    for p in itertools.product(operations, repeat=len):
        permutations.add(p)

    return permutations


def get_expressions(numbers: List[int], operations: List[str]) -> List[List[str]]:
    expressions: List[List[str]] = []

    permutations = ops_permutations(operations, len(numbers) - 1)

    for p in permutations:
        e = make_expression(numbers, list(p))
        expressions.append(e)

    return expressions


class Test(unittest.TestCase):
    def test_make_expression(self):
        numbers = [1, 2, 3, 4]
        operations = ["+", "-", "nothing"]

        self.assertEqual(
            ["1", "+", "2", "-", "3", "nothing", "4"],
            make_expression(numbers, operations),
        )

    def test_evaluate_expression(self):
        numbers = [1, 2, 3, 4]
        operations = ["+", "-", "nothing"]
        expression = make_expression(numbers, operations)

        self.assertEqual(-31, evaluate(expression))

    def test_operations_permutations(self):
        operations = ["+", "-", "nothing"]
        permutations = ops_permutations(operations, 8)
        self.assertEqual(6561, len(permutations))

    def test_get_expressions(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        operations = ["+", "-", "nothing"]
        expressions = get_expressions(numbers, operations)
        self.assertEqual(6561, len(expressions))


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7]
    operations = ["+", "-", "nothing"]
    expressions = get_expressions(numbers, operations)

    for e in expressions:
        result = evaluate(e)
        if result == 70:
            print(str(e) + " = " + str(result))

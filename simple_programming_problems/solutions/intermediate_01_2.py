import unittest
from typing import Any, List


def apply_operations(expression: List[str]) -> int:
    if "nothing" in expression:
        i = expression.index("nothing")
        n1 = expression[i - 1]
        n2 = expression[i + 1]

        expression[i - 1] = "{0}{1}".format(n1, n2)
        del expression[i + 1]
        del expression[i]

        return apply_operations(expression)

    elif "-" in expression:
        i = expression.index("-")
        n = expression[i + 1]

        expression[i + 1] = "-{0}".format(n)
        del expression[i]

        return apply_operations(expression)

    elif "+" in expression:
        i = expression.index("+")

        del expression[i]

        return apply_operations(expression)

    else:
        numbers = [int(element) for element in expression]

        return sum(numbers)


def make_expression(numbers: List[int], operations: List[str]) -> List[Any]:
    expression: List[str] = []

    assert len(operations) == (len(numbers) - 1)

    for i in range(len(operations)):
        expression.append(str(numbers[i]))
        expression.append(operations[i])

    last_number = numbers[-1]
    expression.append(str(last_number))

    return expression


class Test(unittest.TestCase):
    def test_make_expression(self):
        numbers = [1, 2, 3, 4]
        operations = ["+", "-", "nothing"]

        self.assertEqual(
            ["1", "+", "2", "-", "3", "nothing", "4"],
            make_expression(numbers, operations),
        )

    def test_apply_operations(self):
        numbers = [1, 2, 3, 4]
        operations = ["+", "-", "nothing"]
        expression = make_expression(numbers, operations)

        self.assertEqual(-31, apply_operations(expression))

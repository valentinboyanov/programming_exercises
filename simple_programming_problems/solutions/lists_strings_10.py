import unittest
from typing import Any, List

# 10. Write a function that combines two lists by alternatingly taking elements,
# e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].


def combine(a: List[Any], b: List[Any]) -> List[Any]:
    combined_list: List[Any] = []

    a.reverse()
    b.reverse()

    for i in range(len(a) + len(b)):
        if i % 2 == 0:
            if len(a) > 0:
                combined_list.append(a.pop())
            else:
                combined_list.append(b.pop())
        else:
            if len(b) > 0:
                combined_list.append(b.pop())
            else:
                combined_list.append(a.pop())

    return combined_list


class Test(unittest.TestCase):
    def test_same_lenght(self):
        combined = combine(["a", "b", "c"], [1, 2, 3])
        self.assertEqual(["a", 1, "b", 2, "c", 3], combined)

    def test_different_lenght(self):
        self.assertEqual(["a", 1, "b", 2, "c"], combine(["a", "b", "c"], [1, 2]))
        self.assertEqual(["a", 1, "b", "c"], combine(["a", "b", "c"], [1]))
        self.assertEqual(["a", "b", "c"], combine(["a", "b", "c"], []))

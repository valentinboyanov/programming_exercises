import unittest
from typing import Any, List

# 9. Write a function that concatenates two lists: [a,b,c], [1,2,3] → [a,b,c,1,2,3]


def concatenate(a: List[Any], b: List[Any]) -> List[Any]:
    a.extend(b)

    return a


class Test(unittest.TestCase):
    def test_concatenates_list(self):
        joined_list = concatenate(["a", "b", "c"], [1, 2, 3])
        self.assertEqual(["a", "b", "c", 1, 2, 3], joined_list)

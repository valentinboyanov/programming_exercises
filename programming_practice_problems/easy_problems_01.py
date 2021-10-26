import io
import unittest
from typing import List, NamedTuple
from unittest.mock import patch


class Cell(NamedTuple):
    row: int
    col: int
    value: int

    def clue_row(self) -> int:
        text = str(self.value)
        row = int(text[0])
        return row

    def clue_col(self) -> int:
        text = str(self.value)
        col = int(text[1])
        return col

    def coordinates_value(self) -> int:
        return int("{0}{1}".format(self.row, self.col))

    def is_treasure(self) -> bool:
        return self.value == self.coordinates_value()


def explore_for_treasure(map: List[List[int]]) -> None:
    explored_cells: List[Cell] = []

    cell = cell_by_position(map, 1, 1)
    explored_cells.append(cell)

    while cell.is_treasure() != True:
        cell = cell_by_position(map, cell.clue_row(), cell.clue_col())
        explored_cells.append(cell)

    print_path(explored_cells)


def cell_by_position(map: List[List[int]], row: int, col: int) -> Cell:
    value: int = map[row - 1][col - 1]

    return Cell(row, col, value)


def print_path(cells: List[Cell]) -> None:
    print("")
    for cell in cells:
        if cell.is_treasure():
            print("Visited {0}: treasure!".format(cell))
        else:
            print("Visited {0}: clue.".format(cell))


class Test(unittest.TestCase):
    def test_explore_for_treasure_small_map(self):
        map: List[List[int]] = [
            [22, 12, 13],
            [14, 13, 23],
        ]

        expected_output: str = """
Visited Cell(row=1, col=1, value=22): clue.
Visited Cell(row=2, col=2, value=13): clue.
Visited Cell(row=1, col=3, value=13): treasure!
"""

        with patch("sys.stdout", new_callable=io.StringIO) as mocked_out:
            explore_for_treasure(map)
            self.assertEqual(expected_output, mocked_out.getvalue())

    def test_explore_for_treasure_big_map(self):
        map: List[List[int]] = [
            [34, 21, 32, 41, 25],
            [14, 42, 43, 14, 31],
            [54, 45, 52, 42, 23],
            [33, 15, 51, 31, 35],
            [21, 52, 33, 13, 23],
        ]

        expected_output: str = """
Visited Cell(row=1, col=1, value=34): clue.
Visited Cell(row=3, col=4, value=42): clue.
Visited Cell(row=4, col=2, value=15): clue.
Visited Cell(row=1, col=5, value=25): clue.
Visited Cell(row=2, col=5, value=31): clue.
Visited Cell(row=3, col=1, value=54): clue.
Visited Cell(row=5, col=4, value=13): clue.
Visited Cell(row=1, col=3, value=32): clue.
Visited Cell(row=3, col=2, value=45): clue.
Visited Cell(row=4, col=5, value=35): clue.
Visited Cell(row=3, col=5, value=23): clue.
Visited Cell(row=2, col=3, value=43): clue.
Visited Cell(row=4, col=3, value=51): clue.
Visited Cell(row=5, col=1, value=21): clue.
Visited Cell(row=2, col=1, value=14): clue.
Visited Cell(row=1, col=4, value=41): clue.
Visited Cell(row=4, col=1, value=33): clue.
Visited Cell(row=3, col=3, value=52): clue.
Visited Cell(row=5, col=2, value=52): treasure!
"""

        with patch("sys.stdout", new_callable=io.StringIO) as mocked_out:
            explore_for_treasure(map)
            self.assertEqual(expected_output, mocked_out.getvalue())

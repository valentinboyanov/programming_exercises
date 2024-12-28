#                   +-------------------------+
#                   ¦ 34 ¦ 21 ¦ 32 ¦ 41 ¦ 25  ¦
#                   +----+----+----+----+-----¦
#                   ¦ 14 ¦ 42 ¦ 43 ¦ 14 ¦ 31  ¦
#                   +----+----+----+----+-----¦
#                   ¦ 54 ¦ 45 ¦ 52 ¦ 42 ¦ 23  ¦
#                   +----+----+----+----+-----¦
#                   ¦ 33 ¦ 15 ¦ 51 ¦ 31 ¦ 35  ¦
#                   +----+----+----+----+-----¦
#                   ¦ 21 ¦ 52 ¦ 33 ¦ 13 ¦ 23  ¦
#                   +-------------------------+
#
#
# 1. Do you like treasure hunts? In this problem you are to write a program
# to explore the above array for a treasure. The values in the array are clues.
# Each cell contains an integer between 11 and 55; for each value the ten's
# digit represents the row number and the unit's digit represents the column
# number of the cell containing the next clue.
# Starting in the upper left corner (at 1,1), use the clues to guide your
# search of the array. (The first three clues are 11, 34, 42). The treasure is
# a cell whose value is the same as its coordinates. Your program must first
# read in the treasure map data into a 5 by 5 array. Your program should output
# the cells it visits during its search, and a message indicating where you
# found the treasure.


"""
>>> explore_for_treasure([
...     [34, 21, 32, 41, 25],
...     [14, 42, 43, 14, 31],
...     [54, 45, 52, 42, 23],
...     [33, 15, 51, 31, 35],
...     [21, 52, 33, 13, 23],
... ])
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

from typing import List, NamedTuple


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
    """
    >>> explore_for_treasure([
    ...     [22, 12, 13],
    ...     [14, 13, 23],
    ... ])
    Visited Cell(row=1, col=1, value=22): clue.
    Visited Cell(row=2, col=2, value=13): clue.
    Visited Cell(row=1, col=3, value=13): treasure!
    """
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
    for cell in cells:
        if cell.is_treasure():
            print("Visited {0}: treasure!".format(cell))
        else:
            print("Visited {0}: clue.".format(cell))


if __name__ == "__main__":
    map: List[List[int]] = [
        [34, 21, 32, 41, 25],
        [14, 42, 43, 14, 31],
        [54, 45, 52, 42, 23],
        [33, 15, 51, 31, 35],
        [21, 52, 33, 13, 23],
    ]
    explore_for_treasure(map)

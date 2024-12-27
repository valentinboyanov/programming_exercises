# 2. Write a program to search for the "saddle points" in a 5 by 5 array of
# integers. A saddle point is a cell whose value is greater than or equal to
# any in its row, and less than or equal to any in its column. There may be
# more than one saddle point in the array. Print out the coordinates of any
# saddle points your program finds. Print out "No saddle points" if there
# are none.

"""
>>> print_saddle_points([
...     [1, 2, 3, 4, 5],
...     [6, 7, 11, 9, 10],
...     [11, 12, 13, 14, 15],
...     [16, 17, 18, 19, 20],
...     [21, 22, 23, 24, 25],
... ])
Cell(row=1, col=5, value=5, row_values=[1, 2, 3, 4, 5], col_values=[5, 10, 15, 20, 25])
>>> print_saddle_points([
...     [1, 2, 3, 13, 5],
...     [6, 7, 11, 9, 10],
...     [11, 12, 13, 14, 15],
...     [16, 17, 18, 19, 20],
...     [21, 22, 23, 24, 25],
... ])
No saddle points
"""

from typing import List, NamedTuple


class Cell(NamedTuple):
    row: int
    col: int
    value: int
    row_values: List[int]
    col_values: List[int]


def col_values(array: List[List[int]], col: int) -> List[int]:
    values: List[int] = []

    for row in array:
        values.append(row[col])

    return values


def array_to_cells(array: List[List[int]]) -> List[Cell]:
    cells: List[Cell] = []

    for i in range(len(array)):
        for j in range(len(array[i])):
            cell = Cell(
                row=i + 1,
                col=j + 1,
                value=array[i][j],
                row_values=array[i],
                col_values=col_values(array, j),
            )
            cells.append(cell)

    return cells


def is_saddle_point(candidate: Cell) -> bool:
    """
    >>> is_saddle_point(Cell(
    ...     row=4,
    ...     col=4,
    ...     value=5,
    ...     row_values=[1, 2, 3, 4, 5],
    ...     col_values=[5, 10, 15, 20, 25],
    ... ))
    True
    >>> is_saddle_point(Cell(
    ...     row=3,
    ...     col=3,
    ...     value=4,
    ...     row_values=[1, 2, 3, 4, 5],
    ...     col_values=[4, 9, 14, 19, 24],
    ... ))
    False
    """
    max_in_row = candidate.value >= max(candidate.row_values)
    min_in_col = candidate.value <= min(candidate.col_values)

    if max_in_row and min_in_col:
        return True
    else:
        return False


def search_saddle_points(cells: List[Cell]) -> List[Cell]:
    saddle_points: List[Cell] = []

    for c in cells:
        if is_saddle_point(c):
            saddle_points.append(c)

    return saddle_points


def print_saddle_points(array: List[List[int]]) -> None:
    cells = array_to_cells(array)
    saddle_points = search_saddle_points(cells)

    if saddle_points != []:
        for s in saddle_points:
            print(s)
    else:
        print("No saddle points")

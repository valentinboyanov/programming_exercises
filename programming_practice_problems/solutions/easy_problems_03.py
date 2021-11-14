import unittest
from typing import List, NamedTuple

# 3. In the game of chess, a queen can attack pieces which are on the same row,
# column, or diagonal. A chessboard can be represented by an 8 by 8 array.
# A 1 in the array represents a queen on the corresponding square, and a O in
# the array represents an unoccupied square. Your program is to read the
# location of two queens and then update the array appropriately.  Then process
# the board and indicate whether or not the two queens are positioned so that they attack each other.

UNOCCUPIED_SQUARE: int = 0
QUEEN_SQUARE: int = 1


class Chessboard(NamedTuple):
    board: List[List[int]]

    def square(self, x: int, y: int) -> int:
        return self.board[x - 1][y - 1]

    def queen_square(self, x: int, y: int) -> None:
        self.board[x - 1][y - 1] = QUEEN_SQUARE

    def row(self, position: int) -> List[int]:
        return self.board[position - 1]

    def column(self, position: int) -> List[int]:
        return [row[position - 1] for row in self.board]

    def major_diagonal(self, x: int, y: int) -> List[int]:
        squares: List[int] = []

        for p in range(8):
            row_down = x + p
            col_down = y + p
            if row_down <= 8 and row_down > 0 and col_down <= 8 and col_down > 0:
                squares.append(self.board[row_down - 1][col_down - 1])

            row_up = (x - 1) - p
            col_up = (y - 1) - p
            if row_up <= 8 and row_up > 0 and col_up <= 8 and col_up > 0:
                squares.append(self.board[row_up - 1][col_up - 1])

        return squares

    def minor_diagonal(self, x: int, y: int) -> List[int]:
        squares: List[int] = []

        for p in range(8):
            row_down = x + p
            col_down = y - p
            if row_down <= 8 and row_down > 0 and col_down <= 8 and col_down > 0:
                squares.append(self.board[row_down - 1][col_down - 1])

            row_up = (x - 1) - p
            col_up = (y + 1) + p
            if row_up <= 8 and row_up > 0 and col_up <= 8 and col_up > 0:
                squares.append(self.board[row_up - 1][col_up - 1])

        return squares


def make_chessboard() -> Chessboard:
    array_8_x_8: List[List[int]] = []

    for _ in range(8):
        row: List[int] = []
        for _ in range(8):
            row.append(UNOCCUPIED_SQUARE)
        array_8_x_8.append(row)

    return Chessboard(array_8_x_8)


def check_queen_attack(board: Chessboard, x: int, y: int) -> bool:
    row_sum: int = sum(board.row(x))
    column_sum: int = sum(board.column(y))
    main_diagonal_sum: int = sum(board.major_diagonal(x, y))
    antidiagonal_sum: int = sum(board.minor_diagonal(x, y))

    if row_sum > 1 or column_sum > 1 or main_diagonal_sum > 1 or antidiagonal_sum > 1:
        return True
    else:
        return False


class Test(unittest.TestCase):
    def test_add_queens_on_board(self):
        board = make_chessboard()
        board.queen_square(1, 1)
        board.queen_square(8, 8)

        self.assertEqual(1, board.square(1, 1))
        self.assertEqual(1, board.square(8, 8))

    def test_check_attack_on_queens(self):
        board = make_chessboard()
        board.queen_square(1, 1)
        board.queen_square(1, 2)

        self.assertTrue(check_queen_attack(board, 1, 1))
        self.assertTrue(check_queen_attack(board, 1, 2))

    def test_check_no_attack_on_queens(self):
        board = make_chessboard()
        board.queen_square(3, 3)
        board.queen_square(6, 5)

        self.assertFalse(check_queen_attack(board, 3, 3))
        self.assertFalse(check_queen_attack(board, 6, 5))

    def test_sum_diagonals_unoccupied_board(self):
        board = make_chessboard()

        self.assertEqual(0, sum(board.major_diagonal(4, 4)))
        self.assertEqual(0, sum(board.minor_diagonal(4, 4)))

    def test_major_diagonal_sum(self):
        board = make_chessboard()
        board.queen_square(1, 1)

        self.assertEqual(1, sum(board.major_diagonal(1, 1)))

    def test_minor_diagonal_sum(self):
        board = make_chessboard()
        board.queen_square(2, 2)

        self.assertEqual(1, sum(board.minor_diagonal(2, 2)))

import math
import unittest
from typing import List

# 4. One classic method for composing secret messages is called a square code.
# The spaces are removed from the english text and the characters are written
# into a square (or rectangle). For example, the sentence "If man was meant to
# stay on the ground god would have given us roots" is 54 characters long, so
# it is written into a rectangle with 7 rows and 8 columns.
#
#                 ifmanwas
#                 meanttos
#                 tayonthe
#                 groundgo
#                 dwouldha
#                 vegivenu
#                 sroots
#
# The coded message is obtained by reading down the columns going left to right.
# For example, the message above is coded as:
#
# imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau
#
# In your program, have the user enter a message in english with no spaces
# between the words. Have the maximum message length be 81 characters. Display
# the encoded message. (Watch out that no "garbage" characters are printed.)
# Here are some more examples:
#
#  Input                                           Output
# haveaniceday                                    hae and via ecy
# feedthedog                                      fto ehg ee dd
# chillout                                        clu hlt io


def to_square_code(text: str) -> str:
    return to_encoded_message(to_table(text))


def to_table(text: str) -> List[List[str]]:
    table: List[List[str]] = []

    row_len: int = math.ceil((math.sqrt(len(text))))
    row: List[str] = []

    for l in text:
        row.append(l)
        if len(row) == row_len:
            table.append(row)
            row = []

    if row != []:
        table.append(row)

    return table


def to_encoded_message(table: List[List[str]]) -> str:
    code: List[str] = []
    row_len = len(table[0])

    for i in range(row_len):
        col = [row[i] for row in table if len(row) > i]
        text = "".join(col)
        code.append(text)

    return " ".join(code)


class Test(unittest.TestCase):
    def test_text_to_table(self):
        self.assertEqual(
            [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]],
            to_table("abcdefghi"),
        )
        self.assertEqual(
            [["a", "b", "c"], ["d", "e", "f"], ["g", "h"]],
            to_table("abcdefgh"),
        )

    def test_table_to_encoded_message(self):
        self.assertEqual(
            "adg beh cfi",
            to_encoded_message([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]),
        )
        self.assertEqual(
            "adg beh cf",
            to_encoded_message([["a", "b", "c"], ["d", "e", "f"], ["g", "h"]]),
        )

    def test_engislih_to_square_code(self):
        self.assertEqual("hae and via ecy", to_square_code("haveaniceday"))
        self.assertEqual("fto ehg ee dd", to_square_code("feedthedog"))
        self.assertEqual("clu hlt io", to_square_code("chillout"))
        self.assertEqual(
            "imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau",
            to_square_code("ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots"),
        )

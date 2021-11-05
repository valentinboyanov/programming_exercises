import io
import unittest
from typing import List
from unittest.mock import patch

# 19. Write a function that takes a list of strings an prints them,
# one per line, in a rectangular frame. For example
# the list ["Hello", "World", "in", "a", "frame"] gets printed as:
#
# *********
# * Hello *
# * World *
# * in    *
# * a     *
# * frame *
# *********


def rectangular_frame(strings: List[str]) -> None:
    lines: List[str] = []
    content_width: int = max_element_len(strings)

    solid_line_text = character_string(content_width, "*")
    solid_line = line(content_width, solid_line_text, "**", "**")

    lines.append(solid_line)

    for text in strings:
        text_line = line(content_width, text, "* ", " *")
        lines.append(text_line)

    lines.append(solid_line)

    print()
    for l in lines:
        print(l)


def max_element_len(strings: List[str]) -> int:
    max: int = 0

    for s in strings:
        if len(s) > max:
            max = len(s)

    return max


def character_string(size: int, character: str) -> str:
    characters: List[str] = []

    for _ in range(size):
        characters.append(character)

    return "".join(characters)


def line(size: int, body: str, border_left: str, border_right: str) -> str:
    spaces_to_add = size - len(body)
    spaces = [" " for _ in range(spaces_to_add)]
    body_with_spaces = "{0}{1}".format(body, "".join(spaces))

    return border_left + body_with_spaces + border_right


class Test(unittest.TestCase):
    def test_frame_printing(self):
        expected_output: str = """
*********
* Hello *
* World *
* in    *
* a     *
* frame *
*********
"""

        with patch("sys.stdout", new_callable=io.StringIO) as mocked_out:
            rectangular_frame(["Hello", "World", "in", "a", "frame"])
            self.assertEqual(expected_output, mocked_out.getvalue())

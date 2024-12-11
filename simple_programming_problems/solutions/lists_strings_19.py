"""
19. Write a function that takes a list of strings an prints them,
one per line, in a rectangular frame. For example
the list ["Hello", "World", "in", "a", "frame"] gets printed as:

Frame printing
>>> rectangular_frame(["Hello", "World", "in", "a", "frame"])
*********
* Hello *
* World *
* in    *
* a     *
* frame *
*********
"""

from typing import List


def rectangular_frame(strings: List[str]) -> None:
    """
    >>> rectangular_frame(["Hello"])
    *********
    * Hello *
    *********
    """

    lines: List[str] = []
    content_width: int = max_element_len(strings)

    solid_line_text = character_string(content_width, "*")
    solid_line = line(content_width, solid_line_text, "**", "**")

    lines.append(solid_line)

    for text in strings:
        text_line = line(content_width, text, "* ", " *")
        lines.append(text_line)

    lines.append(solid_line)

    for l in lines:
        print(l)


def max_element_len(strings: List[str]) -> int:
    """
    >>> max_element_len(["Hello", "World"])
    5
    """

    max: int = 0

    for s in strings:
        if len(s) > max:
            max = len(s)

    return max


def character_string(size: int, character: str) -> str:
    """
    >>> character_string(3, "*")
    '***'
    """

    characters: List[str] = []

    for _ in range(size):
        characters.append(character)

    return "".join(characters)


def line(size: int, body: str, border_left: str, border_right: str) -> str:
    """
    >>> line(10, "Hello", "* ", " *")
    '* Hello      *'
    """
    spaces_to_add = size - len(body)
    spaces = [" " for _ in range(spaces_to_add)]
    body_with_spaces = "{0}{1}".format(body, "".join(spaces))

    return border_left + body_with_spaces + border_right


if __name__ == "__main__":
    import doctest

    doctest.testmod()

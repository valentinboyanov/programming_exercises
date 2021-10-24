import unittest

# 6. Write a function that tests whether a string is a palindrome.
# Palindrome: a word, verse, or sentence (such as "Able was I ere I saw Elba")
# or a number (such as 1881) that reads the same backward or forward.


def is_palindrome(text: str) -> bool:
    characters = list(text)
    characters.reverse()
    reversed_text = "".join(characters)

    return text.lower() == reversed_text.lower()


class Test(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome("Able was I ere I saw Elba"))
        self.assertTrue(is_palindrome("1881"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("Not a palindrome"))
        self.assertFalse(is_palindrome("1989"))

import unittest
from typing import List

# 20. Write function that translates a text to Pig Latin and back.
# English is translated to Pig Latin by taking the first letter of every word,
# moving it to the end of the word and adding ‘ay’.
# “The quick brown fox” becomes “Hetay uickqay rownbay oxfay”.


def to_pig_latin(text: str) -> str:
    words: List[str] = text.split(" ")

    for i in range(len(words)):
        word = words[i]
        first_letter = word[0]
        cut_word = word.replace(first_letter, "")
        pig_latin_word = cut_word.lower() + first_letter.lower() + "ay"

        if i == 0:
            words[i] = pig_latin_word.capitalize()
        else:
            words[i] = pig_latin_word

    return " ".join(words)


def to_english(text: str) -> str:
    words: List[str] = text.split(" ")

    for i in range(len(words)):
        word = words[i]
        clean_word = word.replace("ay", "")
        last_letter = clean_word[-1]
        cut_word = clean_word.replace(last_letter, "")
        english_word = last_letter.lower() + cut_word.lower()

        if i == 0:
            words[i] = english_word.capitalize()
        else:
            words[i] = english_word

    return " ".join(words)


class Test(unittest.TestCase):
    def test_to_pig_latin(self):
        self.assertEqual(
            "Hetay uickqay rownbay oxfay", to_pig_latin("The quick brown fox")
        )

    def test_to_english(self):
        self.assertEqual(
            "The quick brown fox", to_english("Hetay uickqay rownbay oxfay")
        )

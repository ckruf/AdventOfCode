from pathlib import Path
from typing import Union
from advent.common import yield_lines, INPUTS_FOLDER


INPUT_FILE_NAME = "3.txt"
INPUT_FILE_PATH = Path(INPUTS_FOLDER, INPUT_FILE_NAME)


def calculate_priority_sum(file_path: Union[str, Path]) -> int:
    """
    Function which solves part 1 of the third day challenge on Advent of Code.

    Given a text file, where each line is a string of lower and upper case letters, find the letter present in both
    the first and second half of the string (there is one such letter per line). This letter then gets a priority
    score, 1 through 26 for a-z and 27 through 52 for A-Z. Return the sum of priority scores for the whole file.

    :param file_path: path to input file
    :return: sum of priority scores
    """
    priority_sum = 0

    for line in yield_lines(file_path):
        string = line.strip()
        repeated_letter = find_letter_in_both_halves(string)
        letter_priority_score = get_letter_priority_score(repeated_letter)
        priority_sum += letter_priority_score

    return priority_sum


def find_letter_in_both_halves(string: str) -> str:
    """
    Given a string of even length, find the letter present in both halves of the string.

    :param string: even length string with one letter repeated between its first and second half
    :return: letter present in both halves of string
    """
    str_len = len(string)
    assert str_len % 2 == 0
    half = int(str_len / 2)
    letter_set = set()

    for i in range(half):
        letter_set.add(string[i])

    for i in range(half, str_len):
        if string[i] in letter_set:
            return string[i]


def get_letter_priority_score(letter: str) -> int:
    """
    Convert a letter to a score, ranging 1-26 for a-z and 27-53 A-Z.

    :param letter: a letter
    :return: score
    """
    assert len(letter) == 1
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96


if __name__ == "__main__":
    print(calculate_priority_sum(INPUT_FILE_PATH))

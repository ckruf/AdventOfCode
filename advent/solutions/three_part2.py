from pathlib import Path
from typing import Union, List, Set, Dict
from advent.common import yield_lines, INPUTS_FOLDER
from advent.solutions.three import get_letter_priority_score


INPUT_FILE_NAME = "3.txt"
INPUT_FILE_PATH = Path(INPUTS_FOLDER, INPUT_FILE_NAME)


def calculate_priority_sum(file_path: Union[str, Path]) -> int:
    """
    Function which solves part 2 of the third day challenge on Advent of Code.

    Given a text file, where each line is a string of lower and upper case letter, consider the lines in groups of
    three, and find the letter that these groups have in common (there is one such letter). Note that the letter
    can still repeat multiple times within each line. This letter then gets a priority score, 1 through 26 for a-z and
    27 through 52 for A-Z. Return the sum of priority scores for all groups of three in the whole file.

    :param file_path:
    :return:
    """
    group_size = 3
    counter = 1

    priority_sum = 0

    group_letter_sets: List[Set[str]] = []

    for line in yield_lines(file_path):
        string = line.strip()
        letter_set = set(string)
        group_letter_sets.append(letter_set)

        if counter % group_size == 0:
            common_letter = find_common_letter(group_letter_sets)
            letter_priority_score = get_letter_priority_score(common_letter)
            priority_sum += letter_priority_score
            group_letter_sets = []

        counter += 1

    return priority_sum


def find_common_letter(letter_sets: List[Set[str]]) -> str:
    """
    Given a list of sets containing letters, find the letter present in every set (there should be one such letter).

    :param letter_sets: list of sets each containing letters
    :return: letter found in every single set
    """
    set_count = len(letter_sets)
    letter_counts: Dict[str, int] = dict()

    for letter_set in letter_sets:
        for letter in letter_set:
            letter_occurrences = letter_counts.get(letter, 0)
            if letter_occurrences == set_count - 1:
                return letter
            else:
                letter_counts[letter] = letter_occurrences + 1


if __name__ == "__main__":
    print(calculate_priority_sum(INPUT_FILE_PATH))

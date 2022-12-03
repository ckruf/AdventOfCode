from typing import Union
from pathlib import Path
from advent.common import yield_lines, INPUTS_FOLDER


INPUT_FILE_NAME = "1.txt"
INPUT_FILE_PATH = Path(INPUTS_FOLDER, INPUT_FILE_NAME)


def find_max_calories(file_path: Union[Path, str]) -> int:
    """
    Function which solves part 1 of the first day challenge on Advent of Code.

    Given a text file, where each line is either an integer, or an empty line (only '\n'), find the largest sum of
    a series of consecutive integers uninterrupted by a new line.

    :param file_path: path to input file
    :return: int, the largest sum of uninterrupted integers
    """
    maximum = 0
    current_total = 0

    for line in yield_lines(file_path):
        stripped_line = line.strip()
        if stripped_line:
            current_total += int(stripped_line)
        else:
            if current_total > maximum:
                maximum = current_total
            current_total = 0

    return maximum


def find_top_three_calories(file_path: Union[str, Path]) -> int:
    """
    Function which solves part 2 of first day challenge on Advent of Code.

    Given the same text file as in part 1, rather than finding the single largest uninterrupted sum, find the sum of the
    top three largest uninterrupted sums.


    :param file_path: path to input file
    :return: int, sum of the three largest sums
    """
    top_three = [0, 0, 0]
    current_total = 0

    for line in yield_lines(file_path):
        stripped_line = line.strip()
        if stripped_line:
            current_total += int(stripped_line)
        else:
            in_top_three = False
            for i in range(len(top_three)):
                if current_total > top_three[i]:
                    in_top_three = True
                    beats_index = i
            if in_top_three:
                top_three.insert(beats_index + 1, current_total)
                top_three.pop(0)
            current_total = 0

    return sum(top_three)


if __name__ == "__main__":
    print(find_max_calories(INPUT_FILE_PATH))
    print(find_top_three_calories(INPUT_FILE_PATH))

from pathlib import Path
from typing import Union, NamedTuple, Tuple
from advent.common import yield_lines, INPUTS_FOLDER

INPUT_FILE_NAME = "4.txt"
INPUT_FILE_PATH = Path(INPUTS_FOLDER, INPUT_FILE_NAME)


class Range(NamedTuple):
    begin: int
    end: int


def count_containments(file_path: Union[str, Path]) -> int:
    """
    Function which solves part 1 of the fourth day challenge on Advent of Code.

    Given a text file, where each line contains two ranges of numbers (for example '2-6,4-8'), count the number
    of lines where one of the ranges fully contains the other range.

    :param file_path: path to input file
    :return: count of lines where one range fully contains another
    """
    containment_count = 0

    for line in yield_lines(file_path):
        range_1, range_2 = parse_ranges_line(line)
        if (range_1.begin <= range_2.begin and range_1.end >= range_2.end) or \
                (range_2.begin <= range_1.begin and range_2.end >= range_1.end):
            containment_count += 1

    return containment_count


def count_overlaps(file_path: Union[str, Path]) -> int:
    """
    Function which solves part 2 of the fourth day challenge on Advent of Code.

    Given the same text file containing number ranges, count the number of lines where the ranges overlap.

    :param file_path: path to input file
    :return: count of lines where the ranges overlap
    """
    overlap_count = 0

    for line in yield_lines(file_path):
        range_1, range_2 = parse_ranges_line(line)
        if (range_2.begin <= range_1.begin <= range_2.end) or \
                (range_2.begin <= range_1.end <= range_2.end) or \
                (range_1.begin <= range_2.begin <= range_1.end) or \
                (range_1.begin <= range_2.end <= range_1.end):
            overlap_count += 1

    return overlap_count


def parse_ranges_line(line: str) -> Tuple[Range, Range]:
    """
    Parse string of format '7-91, 12-91', representing two ranges, into two Ranges.

    :param line: string representing two ranges
    :return: tuple of Ranges
    """
    stripped_line = line.strip()
    range_string_1, range_string_2 = stripped_line.split(",")
    range_1 = parse_single_range(range_string_1)
    range_2 = parse_single_range(range_string_2)
    return range_1, range_2


def parse_single_range(range_string: str) -> Range:
    """
    Parse string in format '7-91', representing a range, into a Range.

    :param range_string: string representing a range
    :return: Range
    """
    begin_range, end_range = range_string.split("-")
    return Range(int(begin_range), int(end_range))


if __name__ == "__main__":
    print(count_containments(INPUT_FILE_PATH))
    print(count_overlaps(INPUT_FILE_PATH))

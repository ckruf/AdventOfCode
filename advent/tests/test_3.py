from pathlib import Path
from advent.common import TEST_INPUTS_FOLDER
from advent.solutions.three import calculate_priority_sum
from advent.solutions.three_part2 import calculate_priority_sum as calculate_priority_sum_part2


TEST_INPUT_FILE_NAME = "3.txt"
TEST_INPUT_FILE_PATH = Path(TEST_INPUTS_FOLDER, TEST_INPUT_FILE_NAME)


def test_calculate_priority_sum():
    result = calculate_priority_sum(TEST_INPUT_FILE_PATH)
    assert result == 157


def test_calculate_priority_sum_part_2():
    result = calculate_priority_sum_part2(TEST_INPUT_FILE_PATH)
    assert result == 70

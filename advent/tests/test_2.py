from pathlib import Path
from advent.common import TEST_INPUTS_FOLDER
from advent.solutions.two import calculate_total_score
from advent.solutions.two_part2 import calculate_total_score as calculate_total_score_part2


TEST_INPUT_FILE_NAME = "2.txt"
TEST_INPUT_FILE_PATH = Path(TEST_INPUTS_FOLDER, TEST_INPUT_FILE_NAME)


def test_calculate_total_score():
    result = calculate_total_score(TEST_INPUT_FILE_PATH)
    assert result == 15


def test_calculate_total_score_part_2():
    result = calculate_total_score_part2(TEST_INPUT_FILE_PATH)
    assert result == 12

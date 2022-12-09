from pathlib import Path
from advent.common import TEST_INPUTS_FOLDER
from advent.solutions.eight import count_visible, highest_scenic_score


TEST_INPUT_FILE_NAME = "8.txt"
TEST_INPUT_FILE_PATH = Path(TEST_INPUTS_FOLDER, TEST_INPUT_FILE_NAME)


def test_count_visible():
    result = count_visible(TEST_INPUT_FILE_PATH)
    assert result == 21


def test_highest_scenic_score():
    result = highest_scenic_score(TEST_INPUT_FILE_PATH)
    assert result == 8

from pathlib import Path
from advent.common import TEST_INPUTS_FOLDER
from advent.solutions.one import find_max_calories, find_top_three_calories


TEST_INPUT_FILE_NAME = "1.txt"
TEST_INPUT_FILE_PATH = Path(TEST_INPUTS_FOLDER, TEST_INPUT_FILE_NAME)


def test_find_max_calories():
    result = find_max_calories(TEST_INPUT_FILE_PATH)
    assert result == 8413


def test_find_top_three_calories():
    result = find_top_three_calories(TEST_INPUT_FILE_PATH)
    assert result == 15113

from pathlib import Path
from advent.common import TEST_INPUTS_FOLDER
from advent.solutions.nine import count_visited_positions, count_visited_positions_long_rope


TEST_INPUT_FILE_NAME = "9.txt"
ALT_TEST_INPUT_FILE = "9_1.txt"
TEST_INPUT_FILE_PATH = Path(TEST_INPUTS_FOLDER, TEST_INPUT_FILE_NAME)
ALT_TEST_INPUT_FILE_PATH = Path(TEST_INPUTS_FOLDER, ALT_TEST_INPUT_FILE)


def test_count_visited_positions():
    result = count_visited_positions(TEST_INPUT_FILE_PATH)
    assert result == 13


def test_count_visited_positions_long_rope():
    result = count_visited_positions_long_rope(TEST_INPUT_FILE_PATH)
    assert result == 1


def test_count_visited_positions_long_rope_alt():
    result = count_visited_positions_long_rope(ALT_TEST_INPUT_FILE_PATH)
    assert result == 36

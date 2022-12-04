from pathlib import Path
from advent.common import TEST_INPUTS_FOLDER
from advent.solutions.four import count_containments, count_overlaps


TEST_INPUTS_FILE_NAME = "4.txt"
TEST_INPUTS_FILE_PATH = Path(TEST_INPUTS_FOLDER, TEST_INPUTS_FILE_NAME)


def test_count_containments():
    result = count_containments(TEST_INPUTS_FILE_PATH)
    assert result == 2


def test_count_overlaps():
    result = count_overlaps(TEST_INPUTS_FILE_PATH)
    assert result == 4

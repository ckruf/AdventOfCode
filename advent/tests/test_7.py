from pathlib import Path
from advent.common import TEST_INPUTS_FOLDER
from advent.solutions.seven import find_small_directories, find_smallest_folder_to_delete


TEST_INPUT_FILE_NAME = "7.txt"
TEST_INPUT_FILE_PATH = Path(TEST_INPUTS_FOLDER, TEST_INPUT_FILE_NAME)


def test_find_small_directories():
    result = find_small_directories(TEST_INPUT_FILE_PATH)
    assert result == 95437


def test_find_smallest_to_delete():
    result = find_smallest_folder_to_delete(TEST_INPUT_FILE_PATH)
    assert result == 24933642
import pytest
from pathlib import Path
from advent.common import TEST_INPUTS_FOLDER
from advent.solutions.six import find_first_unique_substring, find_first_unique_substring_combinations,\
    find_first_unique_substring_set


@pytest.mark.parametrize(["test_input_file_name", "output"], [
    ("1", 7),
    ("2", 5),
    ("3", 6),
    ("4", 10),
    ("5", 11)
])
def test_first_unique_substring(test_input_file_name, output):
    test_input_file_path = Path(TEST_INPUTS_FOLDER, f"6_{test_input_file_name}.txt")
    assert find_first_unique_substring(test_input_file_path) == output


@pytest.mark.parametrize(["test_input_file_name", "output"], [
    ("1", 7),
    ("2", 5),
    ("3", 6),
    ("4", 10),
    ("5", 11)
])
def test_first_unique_substring_combinations(test_input_file_name, output):
    test_input_file_path = Path(TEST_INPUTS_FOLDER, f"6_{test_input_file_name}.txt")
    assert find_first_unique_substring_combinations(test_input_file_path) == output


@pytest.mark.parametrize(["test_input_file_name", "output"], [
    ("1", 7),
    ("2", 5),
    ("3", 6),
    ("4", 10),
    ("5", 11)
])
def test_first_unique_substring_set(test_input_file_name, output):
    test_input_file_path = Path(TEST_INPUTS_FOLDER, f"6_{test_input_file_name}.txt")
    assert find_first_unique_substring_set(test_input_file_path) == output


@pytest.mark.parametrize(["test_input_file_name", "output"], [
    ("1", 19),
    ("2", 23),
    ("3", 23),
    ("4", 29),
    ("5", 26)
])
def test_first_unique_substring_part2(test_input_file_name, output):
    test_input_file_path = Path(TEST_INPUTS_FOLDER, f"6_{test_input_file_name}.txt")
    assert find_first_unique_substring(test_input_file_path, 14) == output


@pytest.mark.parametrize(["test_input_file_name", "output"], [
    ("1", 19),
    ("2", 23),
    ("3", 23),
    ("4", 29),
    ("5", 26)
])
def test_first_unique_substring_combinations_part2(test_input_file_name, output):
    test_input_file_path = Path(TEST_INPUTS_FOLDER, f"6_{test_input_file_name}.txt")
    assert find_first_unique_substring_combinations(test_input_file_path, 14) == output


@pytest.mark.parametrize(["test_input_file_name", "output"], [
    ("1", 19),
    ("2", 23),
    ("3", 23),
    ("4", 29),
    ("5", 26)
])
def test_first_unique_substring_set_part2(test_input_file_name, output):
    test_input_file_path = Path(TEST_INPUTS_FOLDER, f"6_{test_input_file_name}.txt")
    assert find_first_unique_substring_set(test_input_file_path, 14) == output

from .constants import TEST_INPUT_LOCATION
from ..solutions.one import find_max_calories, find_top_three_calories


def test_find_max_calories():
    file_location = TEST_INPUT_LOCATION + "1.txt"
    result = find_max_calories(file_location)
    assert result == 8413


def test_find_top_three_calories():
    file_location = TEST_INPUT_LOCATION + "1.txt"
    result = find_top_three_calories(file_location)
    assert result == 15113

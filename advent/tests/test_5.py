from pathlib import Path
from advent.common import TEST_INPUTS_FOLDER, yield_lines
from advent.solutions.five import compute_stack_tops, convert_to_stacks


TEST_INPUT_FILE_NAME = "5.txt"
TEST_INPUT_FILE_PATH = Path(TEST_INPUTS_FOLDER, TEST_INPUT_FILE_NAME)


def test_compute_stack_tops():
    result = compute_stack_tops(TEST_INPUT_FILE_PATH, True)
    assert result == "CMZ"


def test_compute_stack_tops_part_two():
    result = compute_stack_tops(TEST_INPUT_FILE_PATH, False)
    assert result == "MCD"


def test_regex():
    import re
    for line in yield_lines(TEST_INPUT_FILE_PATH):
        letters: list[str] = re.findall("\[(.+?)\]", line)


def test_convert_to_stacks():
    test_input = [
        "    [D]",
        "[N] [C]",
        "[Z] [M] [P]"
        ]
    stacks = convert_to_stacks(test_input, 3)
    assert stacks == [["Z", "N"], ["M", "C", "D"], ["P"]]
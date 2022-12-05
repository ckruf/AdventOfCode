from pathlib import Path
from typing import Union, List
from advent.common import yield_lines, INPUTS_FOLDER
import re

INPUT_FILE_NAME = "5.txt"
INPUT_FILE_PATH = Path(INPUTS_FOLDER, INPUT_FILE_NAME)


def compute_stack_tops(file_path: Union[str, Path], part_1: bool) -> str:
    """
    Function which solves the fifth day challenge on Advent of Code.

    Given a text file, which starts with a representation of three stacks, followed by a sequence of moves of items
    from one stack to another, determine what items will be found at the top of each stack after all the moves have
    been made.

    The initial state of the stacks is represented in this manner:

        [D]
    [N] [C]
    [Z] [M] [P]
     1   2   3

    Each subsequent line then describes a move like so: 'move 1 from 2 to 1', meaning one item would be popped off
    stack 2 and pushed onto stack 1.

    For part 2, when multiple items are moved from one stack to another, they are not popped off one by one,
    but all of them are moved at once.

    :param file_path: path to input file
    :param part_1: bool switch - True for solving part 1, False for solving part 2
    :return: the letters on top of each stack, after all described moves have been completed
    """

    initial_representation: List[str] = []
    moves_reached = False
    stacks: List[List[str]] = []
    last_num = 0

    for line in yield_lines(file_path):
        if moves_reached:
            line_str_numbers: List[str] = re.findall("[0-9]+", line)
            line_numbers: List[int] = list(map(int, line_str_numbers))
            if part_1:
                perform_moves_part1(line_numbers[0], line_numbers[1], line_numbers[2], stacks)
            else:
                perform_move_part2(line_numbers[0], line_numbers[1], line_numbers[2], stacks)

        else:
            if line.strip().startswith("["):
                initial_representation.append(line.rstrip())
            elif line.strip() and line.strip()[0].isnumeric():
                last_num = int(line.split()[-1])
            # there is an empty line between end of intitial stack state and beginning of moves
            elif not line.strip():
                moves_reached = True
                stacks = convert_to_stacks(initial_representation, last_num)
                assert len(stacks) == last_num

    top_letters = []
    for stack in stacks:
        top_letter = stack[-1]
        top_letters.append(top_letter)

    return "".join(top_letters)


def convert_to_stacks(string_representation: List[str], stack_count: int) -> List[List[str]]:
    """
    Given the initial lines of the input file, representing stacks of letters, parse them into a list of lists
    of letters, where each list represents a stack.

    For example, if the file started with the following lines:
        [D]
    [N] [C]
    [Z] [M] [P]

    We would like to parse that to [['Z', 'N'], ['M', 'C', 'D'], ['P']] - three stacks represented as lists
    onto which we can push via append() and from which we can pop via pop().

    :param string_representation: lines from input file, as a list of strings
    :param stack_count: number of stacks
    :return: stacks represented as a list of lists
    """
    stacks: List[List[str]] = []
    for _ in range(stack_count):
        stacks.append(list())

    for line in reversed(string_representation):
        stacks_on_line = int(((len(line) + 1) / 4))
        for j in range(stacks_on_line):
            char_begin = (4 * j) + 1
            char_end = (4 * j) + 2
            char = line[char_begin:char_end]
            stack = stacks[j]
            if char != " ":
                stack.append(char)

    return stacks


def perform_moves_part1(count: int, from_stack_id: int, to_stack_id: int, stacks: List[List[str]]) -> None:
    """
    Perform the moves specified in a line of input. Implements logic for part 1 of the challenge, where
    items are moved one at a time.

    :param count: number of items to move
    :param from_stack_id: which stack to move items from
    :param to_stack_id: which stack to move items to
    :param stacks:
    :return: None
    """
    from_index = from_stack_id - 1
    to_index = to_stack_id - 1

    from_stack = stacks[from_index]
    to_stack = stacks[to_index]

    for _ in range(count):
        moved_item = from_stack.pop()
        to_stack.append(moved_item)


def perform_move_part2(count: int, from_stack_id: int, to_stack_id: int, stacks: List[List[str]]) -> None:
    """
    Perform the moves specified in a line of input. Implements logic for part 2 of the challenge, where
    items are moved several at a time.

    :param count: number of items to move
    :param from_stack_id: which stack to move items from
    :param to_stack_id: which stack to move items to
    :param stacks:
    :return: None
    """
    from_index = from_stack_id - 1
    to_index = to_stack_id - 1
    from_stack = stacks[from_index]
    to_stack = stacks[to_index]

    moved_items = from_stack[-count:]
    to_stack.extend(moved_items)
    # here, we must use 'stacks[from_index]' on the left side of the assignment, rather than
    # 'from_stack', otherwise the original list (stacks) will not be modified
    stacks[from_index] = from_stack[:-count]


if __name__ == "__main__":
    print(compute_stack_tops(INPUT_FILE_PATH, True))
    print(compute_stack_tops(INPUT_FILE_PATH, False))

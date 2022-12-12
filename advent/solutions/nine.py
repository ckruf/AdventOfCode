from pathlib import Path
from advent.common import yield_lines, INPUTS_FOLDER, TEST_INPUTS_FOLDER
from enum import Enum


INPUT_FILE_NAME = "9.txt"
INPUT_FILE_PATH = Path(INPUTS_FOLDER, INPUT_FILE_NAME)
TEST_FILE_PATH = Path(TEST_INPUTS_FOLDER, INPUT_FILE_NAME)


class Direction(Enum):
    RIGHT = "R"
    LEFT = "L"
    UP = "U"
    DOWN = "D"


class Tail:
    x_pos: int
    y_pos: int
    visited_pos: set[tuple[int, int]]

    def __init__(self, x_pos: int = 0, y_pos: int = 0) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.visited_pos = {(self.x_pos, self.y_pos)}

    def make_move(self, x: int, y: int) -> None:
        self.x_pos += x
        self.y_pos += y
        self.visited_pos.add((self.x_pos, self.y_pos))


class Head:
    x_pos: int
    y_pos: int

    def __init__(self, x_pos: int = 0, y_pos: int = 0) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos

    def make_move(self, x: int, y: int) -> None:
        self.x_pos += x
        self.y_pos += y


class Rope:
    head: Head
    tail: Tail

    def __init__(self, head: Head = Head(), tail: Tail = Tail()) -> None:
        self.head = head
        self.tail = tail

    @property
    def y_diff(self):
        return self.head.y_pos - self.tail.y_pos

    @property
    def x_diff(self):
        return self.head.x_pos - self.tail.x_pos

    def process_move(self, direction: Direction, count: int):
        for i in range(count):
            if direction == Direction.RIGHT:
                self.head.make_move(1, 0)
                if self.x_diff > 1:
                    self.tail.make_move(1, self.y_diff)
            elif direction == Direction.LEFT:
                self.head.make_move(-1, 0)
                if self.x_diff < -1:
                    self.tail.make_move(-1, self.y_diff)
            elif direction == Direction.UP:
                self.head.make_move(0, 1)
                if self.y_diff > 1:
                    self.tail.make_move(self.x_diff, 1)
            elif direction == Direction.DOWN:
                self.head.make_move(0, -1)
                if self.y_diff < -1:
                    self.tail.make_move(self.x_diff, -1)
            else:
                raise ValueError("Shouldn't happen")


class Knot:
    x_pos: int
    y_pos: int
    visited_pos: set[tuple[int, int]]

    def __init__(self, x_pos: int = 0, y_pos: int = 0) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.visited_pos = {(self.x_pos, self.y_pos)}

    def make_move(self, x: int, y: int):
        self.x_pos += x
        self.y_pos += y
        self.visited_pos.add((self.x_pos, self.y_pos)

class LongRope:
    knots: list[Knot]

    def __init__(self, length: int) -> None:
        self.knots = []
        for _ in range(length):
            self.knots.append(Knot())
    


def count_visited_positions(file_path: str | Path) -> int:
    """
    Function which solves part 1 of the ninth day challenge on Advent of Code.

    Given an input file containing a series of motions of a rope, return the number of positions tha the tail
    of the rope visited at least once.

    :param file_path:
    :return:
    """
    rope = Rope()
    for line in yield_lines(file_path):
        line = line.strip()
        move_direction, move_count = line.split(" ")
        move_direction = Direction(move_direction)
        move_count = int(move_count)
        rope.process_move(move_direction, move_count)

    return len(rope.tail.visited_pos)


if __name__ == "__main__":
    print(count_visited_positions(INPUT_FILE_PATH))


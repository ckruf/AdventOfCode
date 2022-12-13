from pathlib import Path
from advent.common import yield_lines, INPUTS_FOLDER, TEST_INPUTS_FOLDER
from enum import Enum
from typing import Union


INPUT_FILE_NAME = "9.txt"
SHORT_INPUT_FILE_NAME = "9_short.txt"
INPUT_FILE_PATH = Path(INPUTS_FOLDER, INPUT_FILE_NAME)
SHORT_INPUT_FILE_PATH = Path(INPUTS_FOLDER, SHORT_INPUT_FILE_NAME)
TEST_INPUT_FILE_PATH = Path(TEST_INPUTS_FOLDER, "9_1.txt")


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

    def process_move(self, direction: Direction, count: int) -> None:
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
            print(f"after {direction} move #{i}")
            print(f"head position: ({self.head.x_pos}, {self.head.y_pos})")
            print(f"tail position: ({self.tail.x_pos}, {self.tail.y_pos}")

    def alt_process_move(self, direction: Direction, count: int) -> None:
        for i in range(count):
            if direction == Direction.RIGHT:
                self.head.make_move(1, 0)
            elif direction == Direction.LEFT:
                self.head.make_move(-1, 0)
            elif direction == Direction.UP:
                self.head.make_move(0, 1)
            elif direction == Direction.DOWN:
                self.head.make_move(0, -1)
            else:
                raise ValueError("Shouldn't happen")

            if abs(self.x_diff) > 1:
                if self.x_diff > 1:
                    self.tail.make_move(1, self.y_diff)
                else:
                    self.tail.make_move(-1, self.y_diff)
            if abs(self.y_diff) > 1:
                if self.y_diff > 1:
                    self.tail.make_move(self.x_diff, 1)
                else:
                    self.tail.make_move(self.x_diff, -1)


class Knot:
    x_pos: int
    y_pos: int
    visited_pos: set[tuple[int, int]]

    def __init__(self, x_pos: int = 0, y_pos: int = 0) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.visited_pos = {(self.x_pos, self.y_pos), }

    def make_move(self, x: int, y: int):
        self.x_pos += x
        self.y_pos += y
        self.visited_pos.add((self.x_pos, self.y_pos))

    def print_path(self, y_min: int, y_max: int, x_min: int, x_max: int) -> None:
        for i in range(y_max, y_min, -1):
            if -1 < i < 10:
                print(f" {i}", end=" ")
            else:
                print(i, end=" ")
            for j in range(x_min, x_max):
                if (j, i) in self.visited_pos:
                    print("#", end="")
                else:
                    print(".", end="")

            print()


class LongRope:
    knots: list[Knot]

    def __init__(self, length: int) -> None:
        self.knots = []
        for _ in range(length):
            self.knots.append(Knot())

    def process_move(self, direction: Direction, count: int, line_count: int, silent: bool = True) -> None:
        for _ in range(count):
            for i in range(len(self.knots)):
                if i == 0:
                    if direction == Direction.RIGHT:
                        self.knots[0].make_move(1, 0)
                    elif direction == Direction.LEFT:
                        self.knots[0].make_move(-1, 0)
                    elif direction == Direction.UP:
                        self.knots[0].make_move(0, 1)
                    elif direction == Direction.DOWN:
                        self.knots[0].make_move(0, -1)
                else:
                    x_diff = self.knots[i - 1].x_pos - self.knots[i].x_pos
                    y_diff = self.knots[i - 1].y_pos - self.knots[i].y_pos

                    if abs(x_diff) > 2 and not silent:
                        print(f"x_diff exceeded")
                        print(f"line count {line_count}")
                        print(f"move {direction} #{count}")
                        print(f"position of i ({self.knots[i].x_pos}, {self.knots[i].y_pos})")
                        print(f"position of i-1 ({self.knots[i-1].x_pos}, {self.knots[i-1].y_pos})")
                    if abs(y_diff) > 2 and not silent:
                        print(f"y_diff exceeded")
                        print(f"line count {line_count}")
                        print(f"move {direction} #{count}")
                        print(f"position of i ({self.knots[i].x_pos}, {self.knots[i].y_pos})")
                        print(f"position of i-1 ({self.knots[i - 1].x_pos}, {self.knots[i - 1].y_pos})")

                    if abs(x_diff) > 1:
                        if x_diff > 1:
                            self.knots[i].make_move(1, y_diff)
                        else:
                            self.knots[i].make_move(-1, y_diff)
                    elif abs(y_diff) > 1:
                        if y_diff > 1:
                            self.knots[i].make_move(x_diff, 1)
                        else:
                            self.knots[i].make_move(x_diff, -1)
                if not silent:
                    print(f"after {direction} move #{_}, knot #{i} has position ({self.knots[i].x_pos}, {self.knots[i].y_pos})")

    def alt_process_move(self, direction: Direction, count: int):
        for _ in range(count):
            for i in range(len(self.knots)):
                if i == 0:
                    if direction == Direction.RIGHT:
                        self.knots[0].make_move(1, 0)
                    elif direction == Direction.LEFT:
                        self.knots[0].make_move(-1, 0)
                    elif direction == Direction.UP:
                        self.knots[0].make_move(0, 1)
                    elif direction == Direction.DOWN:
                        self.knots[0].make_move(0, -1)
                else:
                    x_diff = self.knots[i - 1].x_pos - self.knots[i].x_pos
                    y_diff = self.knots[i - 1].y_pos - self.knots[i].y_pos

                    # need to make diagonal move
                    if (x_diff and y_diff) and (abs(x_diff) > 1 or abs(y_diff) > 1):
                        if x_diff < 0:
                            x_move = -1
                        else:
                            x_move = 1

                        if y_diff < 0:
                            y_move = -1
                        else:
                            y_move = 1
                            
                    # non diagonal move
                    else:
                        if x_diff > 1:
                            x_move = 1
                        elif x_diff < -1:
                            x_move = -1
                        else:
                            x_move = 0

                        if y_diff > 1:
                            y_move = 1
                        elif y_diff < -1:
                            y_move = -1
                        else:
                            y_move = 0

                    self.knots[i].make_move(x_move, y_move)


def count_visited_positions(file_path: Union[str, Path]) -> int:
    """
    Function which solves part 1 of the ninth day challenge on Advent of Code.

    Given an input file containing a series of motions of a rope, return the number of positions that the tail
    of the rope visited at least once.

    :param file_path: path to input file containing directions / moves
    :return: count of unique squares the tail of the rope visited at least once
    """
    rope = Rope()
    for line in yield_lines(file_path):
        line = line.strip()
        move_direction, move_count = line.split(" ")
        move_direction = Direction(move_direction)
        move_count = int(move_count)
        rope.alt_process_move(move_direction, move_count)

    return len(rope.tail.visited_pos)


def count_visited_positions_long_rope(file_path: Union[str, Path]) -> int:
    """
    Function which solves part 2 of the ninth day challenge on Advent of Code.

    Given an input file containing a series of motions of a longer rope, return the number of positions positions that
    the tail of the rope visited at least once.

    :param file_path: path to input file containing directions / moves
    :return: count of unique squares the tail of the rope visited at least once
    """
    rope = LongRope(10)
    for line_count, line in enumerate(yield_lines(file_path)):
        line = line.strip()
        move_direction, move_count = line.split(" ")
        move_direction = Direction(move_direction)
        move_count = int(move_count)
        rope.alt_process_move(move_direction, move_count)

    return len(rope.knots[-1].visited_pos)


if __name__ == "__main__":
    print(count_visited_positions_long_rope(TEST_INPUT_FILE_PATH))
    print(count_visited_positions_long_rope(INPUT_FILE_PATH))

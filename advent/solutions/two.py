from typing import Union, Tuple
from pathlib import Path
from enum import Enum
from advent.common import yield_lines, INPUTS_FOLDER


INPUT_FILE_NAME = "2.txt"
INPUT_FILE_PATH = Path(INPUTS_FOLDER, INPUT_FILE_NAME)


class GameElement(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @classmethod
    def from_letter(cls, letter: str):
        if letter in ("A", "X"):
            return cls.ROCK
        elif letter in ("B", "Y"):
            return cls.PAPER
        elif letter in ("C", "Z"):
            return cls.SCISSORS
        else:
            raise ValueError("Letter must be one of A, B, C, X, Y, Z")


class Outcome(Enum):
    WIN = 6
    DRAW = 3
    LOSS = 0


def calculate_total_score(file_path: Union[Path, str]) -> int:
    """
    Function which solves part 1 of the second day challenge on Advent of Code.

    Given a text file, where each line represents a game of rock-paper-scissors, calculate your total score.

    Each line consists of two letters, one A-C, representing the opponent's pick, and one X-Z, representing your own.

    A and X = rock
    B and Y = paper
    C and Z = scissors

    The score for the round is the sum of:
    - the score for the selected shape (rock = 1, paper = 2, scissors = 3)
    - the score for the outcome of the round (loss = 0, draw = 3, win = 6)

    :param file_path: path to input file
    :return: int total score of player 1
    """
    total_score = 0

    for line in yield_lines(file_path):
        p1_letter, p2_letter = parse_player_letters(line)
        p1_choice = GameElement.from_letter(p1_letter)
        p2_choice = GameElement.from_letter(p2_letter)
        round_score = calculate_round_score(p1_choice, p2_choice)
        total_score += round_score

    return total_score


def parse_player_letters(line: str) -> Tuple[str, str]:
    line = line.strip("\n")
    first_letter, second_letter = line.split(" ")
    if first_letter in ("A", "B", "C") and second_letter in ("X", "Y", "Z"):
        p1_letter = second_letter
        p2_letter = first_letter
    elif first_letter in ("X", "Y", "Z") and second_letter in ("A", "B", "C"):
        p1_letter = first_letter
        p2_letter = second_letter
    else:
        raise Exception("unexpected input data format")
    return p1_letter, p2_letter


def calculate_round_score(player_1_choice: GameElement, player_2_choice: GameElement) -> int:
    return calculate_outcome_score(player_1_choice, player_2_choice) + player_1_choice.value


def calculate_outcome_score(player_1_choice: GameElement, player_2_choice: GameElement) -> int:
    if player_1_choice == player_2_choice:
        return Outcome.DRAW.value
    elif player_1_choice == GameElement.ROCK:
        if player_2_choice == GameElement.PAPER:
            return Outcome.LOSS.value
        elif player_2_choice == GameElement.SCISSORS:
            return Outcome.WIN.value
        else:
            raise Exception("something is wrong")
    elif player_1_choice == GameElement.PAPER:
        if player_2_choice == GameElement.ROCK:
            return Outcome.WIN.value
        elif player_2_choice == GameElement.SCISSORS:
            return Outcome.LOSS.value
        else:
            raise Exception("something is wrong")
    elif player_1_choice == GameElement.SCISSORS:
        if player_2_choice == GameElement.PAPER:
            return Outcome.WIN.value
        elif player_2_choice == GameElement.ROCK:
            return Outcome.LOSS.value
        else:
            raise Exception("something is wrong")
    else:
        raise Exception("something is wrong")


if __name__ == "__main__":
    print(calculate_total_score(INPUT_FILE_PATH))

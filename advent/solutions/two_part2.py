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
        if letter == "A":
            return cls.ROCK
        elif letter == "B":
            return cls.PAPER
        elif letter == "C":
            return cls.SCISSORS
        else:
            raise ValueError("Letter must be one of A, B, C")


class Outcome(Enum):
    WIN = 6
    DRAW = 3
    LOSS = 0

    @classmethod
    def from_letter(cls, letter: str):
        if letter == "X":
            return cls.LOSS
        elif letter == "Y":
            return cls.DRAW
        elif letter == "Z":
            return cls.WIN
        else:
            raise ValueError("Letter must be one of X, Y, Z")


def calculate_total_score(file_path: Union[str, Path]) -> int:
    """
    Function which solves part 2 of the second day challenge on Advent of Code.

    Given a text file, where each line represents a game of rock-paper-scissors, calculate your total score.

    Each line consists of two letters, one A-C, representing the opponent's pick, and one X-Z, representing the outcome
    that the game should have (from your perspective)

    A = opponent chooses rock
    B = opponent chooses paper
    C = opponent chooses scissors

    X = you should lose
    Y = you should draw
    Z = you should win

    The score for the round is the sum of:
    - the score for your selected shape (rock = 1, paper = 2, scissors = 3)
    - the score for the outcome of the round (loss = 0, draw = 3, win = 6)

    :param file_path: path to input file
    :return: int total score of player 1
    """
    total_score = 0

    for line in yield_lines(file_path):
        opponent_pick, outcome = parse_line(line)
        my_pick = pick_game_element(opponent_pick, outcome)
        round_score = outcome.value + my_pick.value
        total_score += round_score

    return total_score


def parse_line(line: str) -> Tuple[GameElement, Outcome]:
    line = line.strip("\n")
    first_letter, second_letter = line.split(" ")
    if first_letter in ("A", "B", "C") and second_letter in ("X", "Y", "Z"):
        return GameElement.from_letter(first_letter), Outcome.from_letter(second_letter)
    elif first_letter in ("X", "Y", "Z") and second_letter in ("A", "B", "C"):
        return GameElement.from_letter(second_letter), Outcome.from_letter(first_letter)
    else:
        raise Exception("unexpected input data format")


def pick_game_element(opponent_pick: GameElement, game_outcome: Outcome) -> GameElement:
    """
    Given the opponent's pick in rock-paper-scissors and the supposed outcome of the game,
    return your pick such that the given outcome is reached.

    :param opponent_pick: opponent's pick in rock-paper-scissors game
    :param game_outcome: outcome of game
    :return: your own pick to reach given outcome
    """
    if game_outcome == Outcome.DRAW:
        return opponent_pick
    elif game_outcome == Outcome.WIN:
        if opponent_pick == GameElement.ROCK:
            return GameElement.PAPER
        elif opponent_pick == GameElement.PAPER:
            return GameElement.SCISSORS
        elif opponent_pick == GameElement.SCISSORS:
            return GameElement.ROCK
        else:
            raise Exception("something went wrong")
    elif game_outcome == Outcome.LOSS:
        if opponent_pick == GameElement.ROCK:
            return GameElement.SCISSORS
        elif opponent_pick == GameElement.PAPER:
            return GameElement.ROCK
        elif opponent_pick == GameElement.SCISSORS:
            return GameElement.PAPER
        else:
            raise Exception("something went wrong")
    else:
        raise Exception("something went wrong")


if __name__ == "__main__":
    print(calculate_total_score(INPUT_FILE_PATH))
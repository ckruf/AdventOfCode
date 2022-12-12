from pathlib import Path
from advent.common import yield_lines, INPUTS_FOLDER


INPUT_FILE_NAME = "8.txt"
INPUT_FILE_PATH = Path(INPUTS_FOLDER, INPUT_FILE_NAME)


def count_visible(file_path: str | Path) -> int:
    """
    Function which solves part 1 of the eighth day challenge on Advent of Code.

    Given an input file, representing a grid of trees and their heights, determine how many trees are visible from
    the outside.

    :param file_path: path to input file containing grid of trees
    :return:
    """
    rows, cols = parse_rows_and_cols(file_path)
    visible_count = 0
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if i == 0 or j == 0:
                visible_count += 1
                continue
            visible = is_visible(
                value=rows[i][j],
                x_coordinate=j,
                y_coordinate=i,
                rows=rows,
                cols=cols
            )
            # print(visible)
            if visible:
                visible_count += 1
    return visible_count


def highest_scenic_score(file_path: str | Path) -> int:
    """
    Function which solves part 2 of the eighth day challenge on Advent of Code.

    Given an input file, representing a grid of trees and their heights, find the tree with the highest scenic score.
    The scenic score is calculated by multiplying the number of trees visible when looking each direction.

    :param file_path: path to input file containing grid of trees
    :return: the highest scenic score
    """
    rows, cols = parse_rows_and_cols(file_path)
    max_scenic_score = 0

    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if i == 0 or j == 0:
                continue
            tree_score = scenic_score(
                value=rows[i][j],
                x_coordinate=j,
                y_coordinate=i,
                rows=rows,
                cols=cols
            )
            # print(visible)
            if tree_score > max_scenic_score:
                max_scenic_score = tree_score
    return max_scenic_score



def parse_rows_and_cols(file_path: str | Path) -> tuple[list[list[int]], list[list[int]]]:
    """
    Parse input file into rows and columns.

    :param file_path: path to input file containing grid of trees
    :return: list of rows, list of columns
    """
    rows: list[list[int]] = []
    columns: list[list[int]] = []
    first_line = True
    for line in yield_lines(file_path):
        line = line.strip()
        if first_line:
            for _ in range(len(line)):
                columns.append([])
            first_line = False
        row = []
        for index, char in enumerate(line):
            height = int(char)
            row.append(height)
            columns[index].append(height)
        rows.append(row)
    return rows, columns


def is_visible(
        value: int,
        x_coordinate: int,
        y_coordinate: int,
        rows: list[list[int]],
        cols: list[list[int]]
) -> bool:
    row_length = len(cols)
    col_length = len(rows)

    visible_left = True
    # check visible from the left
    for i in range(x_coordinate - 1, -1, -1):
        if rows[y_coordinate][i] >= value:
            visible_left = False

    if visible_left:
        return True

    visible_right = True
    # check visible from the right
    for i in range(x_coordinate + 1, row_length):
        if rows[y_coordinate][i] >= value:
            visible_right = False

    if visible_right:
        return True

    visible_top = True
    # check visible from the top
    for i in range(y_coordinate - 1, -1, -1):
        if cols[x_coordinate][i] >= value:
            visible_top = False
    if visible_top:
        return True

    visible_bottom = True
    # check visible from the bottom
    for i in range(y_coordinate + 1, col_length):
        if cols[x_coordinate][i] >= value:
            visible_bottom = False
    if visible_bottom:
        return True

    return False


def scenic_score(
        value: int,
        x_coordinate: int,
        y_coordinate: int,
        rows: list[list[int]],
        cols: list[list[int]]
) -> int:
    row_length = len(cols)
    col_length = len(rows)

    score_top = 0
    score_bottom = 0
    score_left = 0
    score_right = 0

    for i in range(x_coordinate - 1, -1, -1):
        score_left += 1
        if rows[y_coordinate][i] >= value:
            break

    for i in range(x_coordinate + 1, row_length):
        score_right += 1
        if rows[y_coordinate][i] >= value:
            break

    # check visible from the top
    for i in range(y_coordinate - 1, -1, -1):
        score_top += 1
        if cols[x_coordinate][i] >= value:
            break

    # check visible from the bottom
    for i in range(y_coordinate + 1, col_length):
        score_bottom += 1
        if cols[x_coordinate][i] >= value:
            break

    return score_left * score_right * score_top * score_bottom



if __name__ == "__main__":
    print(count_visible(INPUT_FILE_PATH))
    print(highest_scenic_score(INPUT_FILE_PATH))

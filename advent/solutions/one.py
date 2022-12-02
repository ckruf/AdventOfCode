FILE_NAME = "../inputs/1.txt"


def find_max_calories(filename: str) -> int:
    """
    Function which solves part 1 of the first day challenge on Advent of Code.

    Given a text file, where each line is either an integer, or an empty line (only '\n'), find the largest sum of
    a series of integers uninterrupted by a new line.

    :param filename: name of input file
    :return: int, the largest sum of uninterrupted integers
    """
    maximum = 0
    current_total = 0

    with open(filename, "r") as reader:
        for line in reader:
            stripped_line = line.strip()
            if stripped_line:
                current_total += int(stripped_line)
            else:
                if current_total > maximum:
                    maximum = current_total
                current_total = 0

    return maximum


def find_top_three_calories(filename: str) -> int:
    """
    Function which solves part 2 of first day challenge on Advent of Code.

    Given the same text file, rather than finding the single largest uninterrupted sum, find the sum of the top three
    largest uninterrupted sums.

    :param filename: name of input file
    :return: int, sum of top three largest sums
    """

    top_three = [0, 0, 0]
    current_total = 0

    with open(filename, "r") as reader:
        for line in reader:
            stripped_line = line.strip()
            if stripped_line:
                current_total += int(stripped_line)
            else:
                in_top_three = False
                for i in range(len(top_three)):
                    if current_total > top_three[i]:
                        in_top_three = True
                        beats_index = i
                if in_top_three:
                    top_three.insert(beats_index + 1, current_total)
                    top_three.pop(0)
                current_total = 0

    return sum(top_three)


if __name__ == "__main__":
    print(find_max_calories(FILE_NAME))
    print(find_top_three_calories(FILE_NAME))
from pathlib import Path
from advent.common import INPUTS_FOLDER, read_file
from queue import Queue
from itertools import combinations
from time import perf_counter_ns

INPUT_FILE_NAME = "6.txt"
INPUT_FILE_PATH = Path(INPUTS_FOLDER, INPUT_FILE_NAME)


def find_first_unique_substring(file_path: str | Path, substr_len: int = 4) -> int:
    """
    Given a string, find the first occurrence of four consecutive unique characters. Return the position of the
    last of the four unique characters. For example, given the string 'mjqjpqmgbljsphdztnvjfqwrcgsmlb', the first
    four consecutive unique characters are 'jpqm' in positions 4-7 (if we start counting from 1). In this case
    we would therefore return 7.

    :param file_path: path to input file
    :param substr_len: length of the unique substring to find
    :return: postion of last letter of first occurence of unique substring
    """
    input_str = read_file(file_path)
    initial_part = input_str[:substr_len]
    main_part = input_str[substr_len:]
    q_letters = Queue()
    counts_letters: dict[str, int] = dict()

    for char in initial_part:
        q_letters.put(char)
        counts_letters[char] = counts_letters.get(char, 0) + 1

    unique = True

    for count in counts_letters.values():
        if count > 1:
            unique = False

    if unique:
        return substr_len

    for position, char in enumerate(main_part, start=(substr_len + 1)):
        unique = True
        removed_letter = q_letters.get()
        count = counts_letters[removed_letter]
        if count == 1:
            counts_letters.pop(removed_letter)
        else:
            counts_letters[removed_letter] = count - 1

        q_letters.put(char)
        counts_letters[char] = counts_letters.get(char, 0) + 1
        for count in counts_letters.values():
            if count > 1:
                unique = False
        if unique:
            return position


def find_first_unique_substring_combinations(file_path: str | Path, substr_len: int = 4) -> int:
    """
    Same as above, but implemented by looking at all possible pairs.

    :param file_path:
    :param substr_len:
    :return:
    """
    input_str = read_file(file_path)
    for i in range(len(input_str) - substr_len):
        unique = True
        pairs = combinations(input_str[i:i+substr_len], 2)
        for pair in pairs:
            if pair[0] == pair[1]:
                unique = False
        if unique:
            return i + substr_len


def find_first_unique_substring_set(file_path: str | Path, substr_len: int = 4) -> int:
    """
    Same as above, but uses sliding window, looking at all 4 characters 'fresh', rather than going through the string
    character by character.

    :param file_path:
    :param substr_len:
    :return:
    """
    input_str = read_file(file_path)
    for i in range(len(input_str) - substr_len):
        unique_count = len(set(input_str[i:i+substr_len]))
        if unique_count == substr_len:
            return i + substr_len


def benchmark(substr_len: int = 4):
    """
    Tests performance of all three functions.

    For part 1, looking for a unique substring of length 4, the results were:
    - queue/dict method: cca 2 million ns
    - set method: cca 250k ns
    - combinations method: cca 600k ns

    For part 2, looking for a unique substring of length 14, the results were:
    - queue/dict method: cca 6.7 million ns
    - set method: cca 1.5 millions ns
    - combinations method: cca 16.5 million ns

    :param substr_len:
    :return:
    """
    substr_fns = [
        find_first_unique_substring,
        find_first_unique_substring_set,
        find_first_unique_substring_combinations
    ]
    for substr_fn in substr_fns:
        start = perf_counter_ns()
        substr_fn(INPUT_FILE_PATH, substr_len)
        end = perf_counter_ns()
        print(f"{substr_fn.__name__} took {end - start} nanoseconds")
    print()


if __name__ == "__main__":
    benchmark(4)
    benchmark(4)
    benchmark(14)
    benchmark(14)

    benchmark(20)
    benchmark(20)

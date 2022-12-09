from __future__ import annotations
from typing import Optional
from pathlib import Path
from advent.common import yield_lines, INPUTS_FOLDER

INPUT_FILE_NAME = "7.txt"
INPUT_FILE_PATH = Path(INPUTS_FOLDER, INPUT_FILE_NAME)


class File:
    name: str
    size: int
    parent: Directory

    def __init__(self, name: str, size: int, parent: Directory | None = None):
        self.name = name
        self.size = size
        self.parent = parent


class Directory:
    name: str
    sub_directories: list[Directory]
    files: list[File]
    parent: Directory
    size: int

    def __init__(
            self,
            name: str,
            parent: Directory,
            files: list[File] = None,
            sub_directories: list[Directory] = None,
            size: int = 0
    ):
        self.name = name
        self.parent = parent
        self.files = files or list()
        self.sub_directories = sub_directories or list()
        self.size = size

    def find_sub_directory(self, dir_name: str) -> False | Directory:
        for directory in self.sub_directories:
            if directory.name == dir_name:
                return directory
        return False

    def find_file(self, file_name: str) -> False | Directory:
        for file in self.files:
            if file.name == file_name:
                return file
        return False


def find_small_directories(file_path: str | Path, max_size: int = 100_000, silent: bool = True) -> int:
    """
    Function which solves part 1 of the seventh day challenge on Advent of Code.

    Given a file which contains a list of commands for navigating a file system ('cd' and 'ls') and their output,
    find all directories whose size is less than the given max_size, and return the sum of the sizes of all of these
    directories.

    :param file_path: path to input file containing commands and their output
    :param max_size: max size of directory to include
    :param silent: print output?
    :return: sum of sizes of all directories whose size is less than max_size
    """
    root = parse_commands_to_file_tree(file_path)
    if not silent:
        print_tree(root)
    calculate_all_directory_sizes(root)
    if not silent:
        print("sizes")
        print_tree_with_sizes(root)
    total_size_small_directories = calculate_sum_small_dir_sizes(root, max_size)
    if not silent:
        print(f"sum of sizes of small directories: {total_size_small_directories}")
    return total_size_small_directories


def find_smallest_folder_to_delete(file_path: str | Path, total_space_needed: int = 30_000_000) -> int:
    """
    Function which solves part 2 of the seveth day challenge on Advent of Code.

    Given a file which contains a list of commands for navigating a file system ('cd' and 'ls') and their output,
    find the smallest directory which, if deleted, will free up enough space.

    :param file_path: path to input file containing commands and their output
    :param total_space_needed: amount of free space needed. This will determine how much needs to be deleted.
    :return:
    """
    total_disk_space = 70_000_000
    root = parse_commands_to_file_tree(file_path)
    calculate_all_directory_sizes(root)
    available_space = total_disk_space - root.size
    additional_space_needed = total_space_needed - available_space
    smallest_size = find_smallest_folder_greater_than(root, additional_space_needed, root.size)
    return smallest_size


def find_smallest_folder_greater_than(root: Directory, additional_space_needed: int, current_smallest_size: int) -> int:
    """
    Find smallest folder in file system whose size is greater than 'additional_space_needed'.

    :param root:
    :param additional_space_needed:
    :param current_smallest_size:
    :return:
    """
    if additional_space_needed < root.size < current_smallest_size:
        current_smallest_size = root.size
    for sub_directory in root.sub_directories:
        current_smallest_size = find_smallest_folder_greater_than(sub_directory, additional_space_needed, current_smallest_size)
    return current_smallest_size


def parse_commands_to_file_tree(file_path: str | Path) -> Directory:
    """
    Given a file which contains a list of commands for navigating a file system ('cd' and 'ls') and their output,
    create a tree strucure of Directory and File objects representing the file system.

    :param file_path: path to input file
    :return: Directory object representing root directory of file system
    """
    current_dir: Optional[Directory] = None
    for line in yield_lines(file_path):
        line = line.strip()
        if line.startswith("$"):
            if line[2:4] == "cd":
                dir_name = line[5:]
                if dir_name == "..":
                    current_dir = current_dir.parent
                else:
                    if not current_dir:
                        current_dir = Directory(name=dir_name, parent=current_dir)
                        continue
                    already_seen_dir = current_dir.find_sub_directory(dir_name)
                    if not already_seen_dir:
                        new_dir = Directory(name=dir_name, parent=current_dir)
                        current_dir.sub_directories.append(new_dir)
                        current_dir = new_dir
                    else:
                        current_dir = already_seen_dir
            elif line[2:4] == "ls":
                continue
            else:
                raise Exception(f"Unknown command {line[2:4]}")
        else:
            if line.startswith("dir"):
                dir_name = line[4:]
                already_seen_dir = current_dir.find_sub_directory(dir_name)
                if not already_seen_dir:
                    new_dir = Directory(name=dir_name, parent=current_dir)
                    current_dir.sub_directories.append(new_dir)
            else:
                file_size, file_name = line.split()
                file_size = int(file_size)
                already_seen_file = current_dir.find_file(file_name)
                if not already_seen_file:
                    new_file = File(file_name, file_size, current_dir)
                    current_dir.files.append(new_file)
    # go to root
    while current_dir.parent:
        current_dir = current_dir.parent
    return current_dir


def print_tree(root: Directory) -> None:
    print(f"current directory: {root.name}")
    print(f"files in current directory:")
    for file in root.files:
        print(file.name)
    print(f"sub-directories in current directory:")
    for sub_directory in root.sub_directories:
        print(sub_directory.name)
    for sub_directory in root.sub_directories:
        print_tree(sub_directory)


def print_tree_with_sizes(root: Directory) -> None:
    print(f"current directory: {root.name}")
    print(f"size: {root.size}")
    for sub_directory in root.sub_directories:
        print_tree_with_sizes(sub_directory)


def calculate_all_directory_sizes(root: Directory) -> int:
    files_size = sum(map(lambda file: file.size, root.files))
    sub_directories_size = 0
    for sub_directory in root.sub_directories:
        sub_directories_size += calculate_all_directory_sizes(sub_directory)
    total_size = files_size + sub_directories_size
    root.size = total_size
    return total_size


def calculate_sum_small_dir_sizes(root: Directory, folder_max_size: int = 100_000) -> int:
    total_size_small_directories = 0
    if root.size <= folder_max_size:
        total_size_small_directories += root.size
    for sub_directory in root.sub_directories:
        total_size_small_directories += calculate_sum_small_dir_sizes(sub_directory, folder_max_size)
    return total_size_small_directories


if __name__ == "__main__":
    print(find_smallest_folder_to_delete(INPUT_FILE_PATH))

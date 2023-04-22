import os
import shutil
from typing import Union
import argparse


def find_files(path: str = '.') -> list:
    """
    Find all files in directory
    :param path: Path to search, may be relative or absolute
    :return: list with files names, if path was relative file names are relative too
    """
    if path[:-1] != "/":
        path += "/"

    return [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]


def deduplicate_list(lst: list) -> list:
    """
    Create a list only with unique elements from lst
    :param lst: Base list
    :return: List with only unique elements
    """
    dct = dict.fromkeys(lst)
    if '' in dct:  # remove empty elements only if empty element exist
        del dct['']
    return list(dct)


def insert_version_to_filename(filename: str, version: int) -> str:
    """
    Insert file version to before file extension,
    if there is no file extension if file name version will be added at end

    for ex:
    filename: doc.txt
    version: 3
    return: doc(3).txt
    :param filename: Name of file
    :param version: File version (only integers)
    :return:
    """
    if '.' in filename:
        s = filename.split('.')
        s[0] += "(" + str(version) + ")"
        return s[0] + "." + s[1]
    else:
        return filename + "(" + str(version) + ")"


def find_prefix_suffix(word: str, prefix_only: bool = False) -> Union[str, list]:
    """
    Cut string to number
    :param word: Word to cut
    :param prefix_only: set to True to get only left side of a word
    :return: list of left and right side of string, or only left side of string
    """
    prefix = ""
    suffix = ""
    flag = False

    if word[0].isdigit() or not word[0].isalnum():
        prefix = word[0]
        suffix = word[1:]
        if prefix_only:
            return prefix
        return [prefix, suffix]

    for char in word:
        if ord(char) < 65:
            flag = True
        if flag:
            suffix += char
        else:
            prefix += char

    if prefix_only:
        return prefix
    return [prefix, suffix]


def find_unique_prefixes(files: list) -> list:
    """
    Find unique prefixes in file list

    Prefix is a part of file name from start to first number or special char,
    if file name contain only numbers prefix is a first char
    :param files: list of files
    :return: list of unique prefixes
    """
    prefixes = []
    for f in files:
        prefixes.append(find_prefix_suffix(f, prefix_only=True))

    return deduplicate_list(prefixes)


def create_directories(dirs: list, path: str = "./", verbose: bool = True) -> None:
    """
    Create directories from provided names

    If path variable is specified directories will be created in that path
    :param dirs: directories names
    :param path: option path
    :param verbose: Verbose output
    """
    # forgotten slash protection
    if path[:-1] != "/":
        path += "/"

    for dir_name in dirs:
        if verbose:
            print('Make dir: ', os.path.join(path, dir_name))
        os.makedirs(name=os.path.join(path, dir_name), exist_ok=True)


def move_files(files: list, path: str = "./", avoid_main: bool = True, verbose: bool = True, overwrite: bool = False,
               max_try: int = 10):
    """
    Move files from path to 'path/prefix/',

    path is optional if no provided local relative path will be used
    :param files: Files to move (targets)
    :param path: Destination path
    :param avoid_main: Do nothing with file names "main.py"
    :param verbose: Verbose output
    :param overwrite: Overwrite destination file
    :param max_try: Maximum number of copy tries
    """
    if path[:-1] != "/":
        path += "/"

    for file in files:
        if file != "main.py" and avoid_main:  # main.py probably isn't file provided to sort
            if verbose:
                print("Move: ", file)
            if os.path.exists(os.path.join(path, find_prefix_suffix(file, True), file)):
                if verbose:
                    print("File exist: ", file)
                if overwrite:
                    shutil.move(os.path.join(path, file), os.path.join(path, find_prefix_suffix(file, True), file))
                    print("File overwrite: ", file)
                else:
                    for i in range(0, max_try):
                        shutil.move(os.path.join(path, file), os.path.join(path, find_prefix_suffix(file, True),
                                                                           insert_version_to_filename(file, i)))

            else:
                shutil.move(os.path.join(path, file), os.path.join(path, find_prefix_suffix(file, True), file))


def ask_user(no_files: int, no_dirs: int) -> bool:
    """
    Ask use to continue
    :param no_files: number of moved files
    :param no_dirs: number of create directories
    :return:
    """
    print(no_files, " file will be moved", no_dirs, " directories will be created")
    ans = input("Continue? [n/Y] ")
    if ans == 'n':
        return False
    else:
        return True


def get_args() -> dict:
    """
    Get command line arguments
    :return:
    """
    parser = argparse.ArgumentParser(prog="File sorter", description="File sorting utility")
    parser.add_argument('path', help="Path to sort")
    parser.add_argument('-a', '--avoid-main', action='store_true', help='Do nothing with file named "main.py"')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    parser.add_argument('-y', '--yes', action='store_true', help="Do not ask to continue")
    parser.add_argument('-o', '--overwrite', action='store_true',
                        help="Overwrite file if file in destination already exist")
    parser.add_argument('-m', '--max-try', type=int, help="Maximum number of copy tries", default=10)
    args = parser.parse_args()

    opt = {'path': args.path,
           'avoid_main': args.avoid_main,
           'verbose': args.verbose,
           'yes': args.yes,
           'overwrite': args.overwrite,
           'maxTry': args.max_try}
    return opt


def run() -> None:
    """
    Run script
    """
    args = get_args()

    files = find_files(path=args['path'])
    # TODO: check if directory exist (only because this number of directories is used in ask user)
    dirs = find_unique_prefixes(files=files)

    if not args['yes']:
        if not ask_user(len(files), len(dirs)):
            exit(3)

    create_directories(dirs, path=args['path'], verbose=args['verbose'])
    move_files(files=files, path=args['path'], verbose=args['verbose'], overwrite=args['overwrite'],
               max_try=args['maxTry'])


if __name__ == "__main__":
    run()

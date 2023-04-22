from pdfrw import PdfReader
import argparse
import os
import re


def find_pdfs(path: str = ".") -> list:
    """
    Find every .pdf file in provided path
    :param path: path to search for .pdf
    :return:
    """
    files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file)) and '.' in file and
            (file.split('.')[1] == 'pdf' or file.split('.')[1] == 'PDF')]
    return files


def rename_file(file: str, new: str, path: str) -> None:
    old_file = os.path.join(path, file)

    new_file = os.path.join(path, (new + ".pdf"))
    print(new)
    os.rename(old_file, new_file)


def fix_title(title):
    exclude_chars = '[<>:"/|?*]'
    if not title:
        return ""
    if title.startswith("("):
        title = title[1:]
    if title.endswith(")"):
        title = title[:-1]

    title = re.sub(exclude_chars, "", title)
    title = re.sub(r"\\", "", title)
    title = re.sub("\n", "", title)

    return title


def extract_title(file: str, path: str = ".") -> str:
    reader = PdfReader(os.path.join(path, file))
    return fix_title(reader.Info.Title)


def sanitise_path(path: str) -> str:
    """
    Sanitise path argument
    :param path:
    :return:
    """
    if path[-1:] != '/':
        path = path + '/'
    return path


def get_args() -> dict:
    parser = argparse.ArgumentParser(prog="PDFTitleExtractor", description="Title extractor/file renamer for pdf")
    parser.add_argument('path', help="Working directory")
    args = parser.parse_args()
    opts = {
        'path': sanitise_path(args.path),
    }
    return opts


def ask_user(op_no: int) -> bool:
    a = input(str(op_no) + " files will be renamed, continue? [Y/n]")
    if a == 'n':
        return False
    return True


def run():
    args = get_args()
    pdfs = find_pdfs(path=args['path'])
    if ask_user(len(pdfs)):
        for pdf in pdfs:
            try:
                title = extract_title(file=pdf, path=args['path'])
                if title != "":
                    rename_file(file=pdf, new=title, path=args['path'])
            except ValueError:
                print("Can't process", pdf)


if __name__ == "__main__":
    run()

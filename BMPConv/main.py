#!/bin/python3
import os
import argparse
from datetime import datetime
from PIL import Image
import PIL.ImageOps

def get_bmp(path: str = ".") -> list:
    """
    Find every .bmp file in provided path
    :param path: path to search for .bmp
    :return:
    """
    return [file for file in os.listdir(path)
            if os.path.isfile(os.path.join(path, file)) and
            '.' in file and
            (file.split('.')[1] == 'BMP' or file.split('.')[1] == 'bmp')]


def mkdir(path: str = "./") -> str:
    """
    Create directory where converted files will be stored
    :return:
    """
    time_stamp = datetime.now().strftime("%H_%M_%S-%d-%m-%y")
    dir_name = path + "cnv_" + time_stamp
    os.mkdir(dir_name)
    return dir_name


def convert(image: str, destination: str, extension: str, invert: bool = False) -> None:
    """
    Convert image
    :param image: image path
    :param destination: path to store converted image
    :param extension: extension to convert image into
    :param invert: set true to inver colors
    :return:
    """
    name_without_ext = image.split('.')[0]
    im = Image.open(image)
    if invert:
        im = PIL.ImageOps.invert(im)
    im.save(destination+"/"+name_without_ext + extension)


def sanitise_extensions(ext: str) -> str:
    """
    Check if extension is valid (in terms of this script)
    :param ext: extension to check
    :return: ext if valid or .png if ext is not valid
    """
    if type(ext) != str:
        return '.png'
    available_extensions = ['.jpg', '.png']
    if ext[0] != '.':
        ext = '.' + ext
    for a_ext in available_extensions:
        if ext == a_ext:
            return ext
    return ".png"


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
    """
    Parse arguments from user
    :return:
    """
    parser = argparse.ArgumentParser(prog="BMPConv", description="BMP converter")
    parser.add_argument('path', help="Working directory")
    parser.add_argument('-e', '--extension', type=str, help='target extension')
    parser.add_argument('-i', '--invert', action='store_true', help='invert colors')
    args = parser.parse_args()
    opts = {
            'path': sanitise_path(args.path),
            'ext': sanitise_extensions(args.extension),
            'inv': args.invert
            }
    return opts


def app():
    """
    Run application
    :return:
    """
    args = get_args()
    destination = mkdir(path=args['path'])
    bmp_files = get_bmp(path=args['path'])
    for bmp in bmp_files:
        convert(bmp, destination, extension=args['ext'], invert=args['inv'])


if __name__ == '__main__':
    app()


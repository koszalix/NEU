# FileSorter
A script for sorting files, designed specially for datasheets of electronics parts.

## How it works
This script basically move files to directories based on file prefixes. File prefix is s a part of file name from 
start to first number or special char. It may seem strange, but it has a lot of sense for datasheets of electronics parts.
### Let's see an example:

In directory there are files:    
 - TL061.pdf
 - TL062.pdf
 - LM358.pdf
 - LM339.pdf
 - OP07.pdf

After script run the directory tree will look like this:
  - TL
    - TL061.pdf
    - TL062.pdf
  - LM
    - LM358.pdf
    - LM339.pdf
  - OP
    - OP07.pdf

## How to use it
1. Install Python interpreter
2. Download `main.py` 
3. Open terminal and run `python main.py <path to sort>`
4. There is more option you can read about it by running `python main.py -h`

## Installation on Windows
On Windows installation can be done automagically by running `InstallOnWindows.ps1`
all program files are stored in %appdata%/FileSorter. Installation script for Linux will be added soon
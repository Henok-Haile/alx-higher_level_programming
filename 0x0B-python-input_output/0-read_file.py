#!/usr/bin/python
"""Defines a fucntion that reads a text file"""


def read_file(filename=""):
    """prints the contents of a utf8 text file to the stdout.
    
    Args:
        filename: The path to the file to read.

    Returns:
        None.

    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")

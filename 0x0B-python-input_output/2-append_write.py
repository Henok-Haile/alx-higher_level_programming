#!/usr/bin/python3
"""Defines a function that appends a text file."""


def append_write(filename="", text=""):
    """Appends a string to utf-8 text file.

    Args:
        filename (str): The name of the file to be appended.
        text (str): the contents to be appended to the file.

    Returns:
        the number of characters appended.

    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return (file.write(text))

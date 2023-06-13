#!/usr/bin/python3
"""Defines a function that writes a text file."""


def write_file(filename="", text=""):
    """Writes a string to utf-8 text file.

    Args:
        filename (str): The name of the file to be written.
        text (str): the contents to be written to the file.

    Returns:
        the number of characters written.

    """
    with open(filename, "w", encoding="utf-8") as file:
        return (file.write(text))

#!/usr/bin/python3
"""Create a Class Square"""


class Square:
    """A class Square"""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size: size of the square created
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

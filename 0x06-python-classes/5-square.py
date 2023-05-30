#!/usr/bin/python3
"""create a class Square."""


class Square:
    """A Class Square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size: size of the created square.
        """
        self.size = size

    @property
    def size(self):
        """retrive the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns current area of the square."""
        return (self.__size ** 2)

    def my_print(self):
        """prints a square with # character"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")

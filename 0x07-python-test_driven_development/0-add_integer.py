#!/usr/bin/python3
# 0-add_integer.py
# Henok H Ghebreweldi <henokhail53@gmail.com>

"""Defines a function of integer Addition."""


def add_integer(a, b=98):
    """Returns integer addition of a and b.

    Float arguments are first casted to integers before addition.

    Raises:
        TypeError: If a or b is not integere or float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

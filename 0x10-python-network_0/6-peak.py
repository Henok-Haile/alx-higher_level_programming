#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """A function that finds a peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    else:
        return max(list_of_integers)

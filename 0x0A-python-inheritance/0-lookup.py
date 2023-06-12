"""Defines object attribute lookup function."""


def lookup(obj):
    """Returns list of available object attributes."""
    return (dir(obj))

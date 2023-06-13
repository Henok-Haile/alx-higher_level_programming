#!/usr/bin/python3
"""Defines JSON-to-object function."""
import json


def from_json_string(my_str):
    """Return the python object representation of a json string."""
    return json.loads(my_str)

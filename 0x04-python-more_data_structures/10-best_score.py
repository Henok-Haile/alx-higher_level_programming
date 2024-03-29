#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    initial_num = list(a_dictionary.keys())[0]
    large = a_dictionary[initial_num]
    for key, value in a_dictionary.items():
        if value > large:
            large = value
            initial_num = key
    return initial_num

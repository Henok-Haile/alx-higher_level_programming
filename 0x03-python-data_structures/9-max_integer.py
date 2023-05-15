#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None
    large_number = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > large_number:
            large_number = my_list[i]

    return large_number

#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if bool(my_list) is not False:
        my_list.reverse()
        for i in my_list:
            print("{:d}".format(i))

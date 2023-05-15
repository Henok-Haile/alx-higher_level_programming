#!/usr/bin/python3

def no_c(my_string):
    # new_string = [x for x in my_string if x != 'c' and x != 'C']

    new_string = []
    for x in range(len(my_string)):
        if (my_string[x] != 'c' and my_string[x] != 'C'):
            # new_string.insert(x, my_string[x])
            new_string.append(my_string[x])
    
    return ("".join(new_string))

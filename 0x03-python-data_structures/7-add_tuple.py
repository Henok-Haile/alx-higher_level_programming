#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    new_list = []
    if len(list_a) == 0:
        list_a == [0, 0]
    elif len(list_a) == 1:
        list_a = [list_a[0], 0]
    else:
        list_a

    if len(list_b) == 0:
        list_b = [0, 0]
    elif len(list_b) == 1:
        list_b = [list_b[0], 0]
    else:
        list_b
    for i in range(len(list_a)):
        for j in range(len(list_b)):
            if j == i:
                new_list.append(list_a[i] + list_b[j])

    new_tuple = tuple(new_list)

    return new_tuple

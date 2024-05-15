#!/usr/bin/python3
#7-add_tuple.py

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Function that adds 2 tuples.
    """
    len_tuple_a = len(tuple_a)
    len_tuple_b = len(tuple_b)
    new_tuple = ()

    if len_tuple_a < 2:
        if len_tuple_a == 0:
            tuple_a = (0, 0)
        else:
            tuple_a = (tuple_a[0], 0)
    if len_tuple_b < 2:
        if len_tuple_b == 0:
            tuple_b = (0, 0)
        else:
            tuple_b = (tuple_b[0], 0)

    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return (new_tuple)

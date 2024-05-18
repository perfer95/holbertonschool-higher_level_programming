#!/usr/bin/python3
# 11-multiply_list_map.py

def multiply_list_map(my_list=[], number=0):
    """
    function that returns a list with all values multiplied by a number without
    using any loops.
    """
    new_list = list(map((lambda val: val * number), my_list))

    return new_list

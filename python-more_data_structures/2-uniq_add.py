#!/usr/bin/python3
# 2-uniq_add.py

def uniq_add(my_list=[]):
    """
    function that adds all unique integers in a
    list (only once for each integer).
    """
    set_list = set(my_list)
    sum_list = 0

    for i in set_list:
        sum_list += int(i)

    return sum_list

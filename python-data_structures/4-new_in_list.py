#!/usr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    """
     function that replaces an element in a list at a specific
     position without modifying the original list
    """
    new_list = my_list[:]
    len_list = len(my_list)

    if idx < 0 or idx > (len_list - 1):
        return new_list
    else:
        new_list[idx] = element
        return new_list

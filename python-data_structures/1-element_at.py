#!/usr/bin/python3
# 1-element_at.py

def element_at(my_list, idx):
    """
    Function that retrieves an element from a list.
    """
    len_list = len(my_list)

    if idx  < 0 or idx > (len_list - 1):
        return None
    else:
        return my_list[idx]

#!/usr/bin/python3
# 11-delete_at.py

def delete_at(my_list=[], idx=0):
    """
    function that deletes the item at a specific position in a list.
    """
    new_list = []

    for i in range(0, len(my_list)):
        if i != idx:
            new_list.append(my_list[i])

    return new_list

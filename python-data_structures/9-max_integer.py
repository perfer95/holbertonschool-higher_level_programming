#!/usr/bin/python3
# 9-max_integer.py

def max_integer(my_list=[]):
    """
    Function that finds the biggest integer of a list.
    """
    val_max = 0

    if my_list == []:
        return None
    
    val_max = my_list[0]

    for i in range(1, len(my_list)):
        if val_max < my_list[i]:
            val_max = my_list[i]

    return val_max
        

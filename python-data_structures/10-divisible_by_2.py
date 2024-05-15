#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(my_list=[]):
    """
    Function that finds all multiples of 2 in a list.
    """
    new_list = []

    if my_list == []:
        return None

    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)

    return new_list

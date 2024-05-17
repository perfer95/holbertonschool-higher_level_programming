#!/usr/bin/python3
# 1-search_replace.py

def search_replace(my_list, search, replace):
    """
    function that replaces all occurrences of an element by another
    in a new list.
    """
    return [val if (val != search) else repalce for val in my_list]

#!/usr/bin/python3
# 101-remove_char_at.py

def remove_char_at(str, n):
    """
     function that creates a copy of the string, removing
     the character at the position n
    """
    new_str = str[:n] + str[n+1:]

    return (new_str)

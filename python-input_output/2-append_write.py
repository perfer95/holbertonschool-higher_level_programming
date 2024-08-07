#!/usr/bin/python3
"""
2. Append to a file
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and
    returns the number of characters added
    """
    with open(filename, "a", encoding="UTF-8") as file:
        len_add_char = file.write(text)

    return len_add_char

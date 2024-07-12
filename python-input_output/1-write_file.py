#!/usr/bin/python3
"""
1. Write to a file
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8) and returns
    the number of characters written
    """
    with open(filename, "w", encoding="UTF-8") as file:
        file.write(text)

    return len(text)

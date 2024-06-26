#!/usr/bin/python3
"""
5-text_indentation.py
"""


def text_indentation(text):
    """
    def text_indentation(text): ".", "?" and ":"
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start = 0
    end = 0

    for i in text:
        if i in ".?:" or ((end + 1) == len(text)):
            if text[start] == " ":
                start += 1
            end += 1
            print(text[start:end])
            start = end
            if i in ".?:":
                print("")
        else:
            end += 1

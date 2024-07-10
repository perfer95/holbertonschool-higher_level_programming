#!/usr/bin/python3
"""
10. Square #1
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square Representation """
    def __init__(self, size):
        """ Cosntructor """
        self.integer_validator("size", size)
        self.__size = size

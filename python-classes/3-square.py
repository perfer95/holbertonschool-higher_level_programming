#!/usr/bin/python3
# 3-square.py
"""
Define class Square
"""


class Square:
    """
    Defines a square:
    """

    def __init__(self, size=0):
        """
        New Square

        Args:
            size: size of square (int)
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """
        Return the area of the square
        """
        return self.__size * self.__size

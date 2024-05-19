#!/usr/bin/python3
# 4-square.py
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
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, val):
        if type(val) != tuple or len(val) != 2 or type(val[0]) != int\
           or type(val[1]) != int or val[0] < 0 or val[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = val

    def area(self):
        """
        Return the area of the square
        """
        return self.__size * self.__size

    def my_print(self):
        if self.__size is 0:
            print("")
        else:
            print('\n' * self.__position[1], end='')
            for num in range(0, self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)

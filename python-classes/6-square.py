#!/usr/bin/python3
# 4-square.py
"""
Define class Square
"""


class Square:
    """
    Defines a square:
    """

    def __init__(self, size=0, position=(0,0)):
        """
        New Square

        Args:
            size: size of square (int)
            position: The position of the square (int, int)
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

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
        """
        Print the squaer whit #
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(0, self.__position[1]):
                print("")
            for i in range(0, self.__size):
                for j in range(0, self.__position[0]):
                    print(" ", end="")
                for k in range(0, self.__size):
                    print("#", end="")
                print("")

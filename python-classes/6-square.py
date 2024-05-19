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
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

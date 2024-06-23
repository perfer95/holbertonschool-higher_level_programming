#!/usr/bin/python3

"""
2-matrix_divided.py
#Remeber two spaces erase this before
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.
    """
    """
    Verify if is matrix and each element is an integers/floats
    - Verify if matrix is a list
    - Verify if each element of matrix is a list
    - Verify if is an empty matrix
    """
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            matrix == []):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    """
    Verify if each element is an integers/floats
    """
    for i in matrix:
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")
    """
    Each row of the matrix must be the same size
    """
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    """
    div must be a number (integer or float)
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    """
    div can’t be equal to 0
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])

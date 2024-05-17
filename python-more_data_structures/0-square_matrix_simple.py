#!/usr/bin/python3
# 0-square_matrix_simple.py

def square_matrix_simple(matrix=[]):
    """
    Function that computes the square value of all integers of a matrix.
    """
    return [list(map(lambda val: val * val, element)) for element in matrix]

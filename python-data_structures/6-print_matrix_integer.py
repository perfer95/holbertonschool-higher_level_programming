#!/usr/bin/python3
# 6-print_matrix_integer.py

def print_matrix_integer(matrix=[[]]):
    """
    Function that prints a matrix of integers.
    """

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if j != (len(matrix[i]) - 1):
                print("{:d} ".format(matrix[i][j]), end="")
            else:
                print("{:d}".format(matrix[i][j]))
    if (len(matrix) == 0) and (len(matrix[i]) == 0):
        print("")

#!/usr/bin/python3
# 6-print_matrix_integer.py

def print_matrix_integer(matrix=[[]]):
    """
    Function that prints a matrix of integers.
    """

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="")
            if j != (len(matrix[i]) - 1):
                print(" ", end="")

        print("")  # print \n

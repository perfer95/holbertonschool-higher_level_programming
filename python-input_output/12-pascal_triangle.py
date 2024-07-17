#!/usr/bin/python3
"""
12. Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascals triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) != n:
        a = triangle[-1]
        b = [1]
        for i in range(len(a) - 1):
            b.append(a[i] + a[i + 1])
        b.append(1)
        triangle.append(b)

    return triangle

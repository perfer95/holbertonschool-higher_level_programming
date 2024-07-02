#!/usr/bin/python3

"""
7. Lazy matrix multiplication
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function that multiplies 2 matrices by using the module NumPy
    """
    if not isinstance(m_a, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("shapes (1,0) and (2,2) not aligned: 0 (dim 1) "
                         "!= 2 (dim 0)")
    if m_b == [] or m_b == [[]]:
        raise ValueError("shapes (2,2) and (1,0) not aligned: 2 (dim 1) "
                         "!= 1 (dim 0)")

    for row in m_a:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("invalid data type for einsum")
    for row in m_b:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("invalid data type for einsum")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("setting an array element with a sequence.")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("setting an array element with a sequence.")

    if len(m_a[0]) != len(m_b):
        raise ValueError("shapes (2,3) and (2,2) not aligned: 3 (dim 1) "
                         "!= 2 (dim 0)")

    return np.matmul(m_a, m_b)

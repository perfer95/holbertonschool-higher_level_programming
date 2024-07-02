#!/usr/bin/python3

"""
7. Lazy matrix multiplication
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function that multiplies 2 matrices by using the module NumPy
    """
    a = np.array(m_a)
    b = np.array(m_b)

    return np.matmul(a, b)

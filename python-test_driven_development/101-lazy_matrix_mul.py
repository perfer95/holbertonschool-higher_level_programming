#!/usr/bin/python3

"""
7. Lazy matrix multiplication
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Function that multiplies 2 matrices by using the module NumPy
    """
    return numpy.matrix(m_a) * numpy.matrix(m_b)

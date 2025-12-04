#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy."""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    # Validate m_a
    if not isinstance(m_a, list) or m_a == [] or m_a == [[]]:
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    if not isinstance(m_b, list) or m_b == [] or m_b == [[]]:
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    # Validate elements inside
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("Scalar operands are not allowed, use '*' instead")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("Scalar operands are not allowed, use '*' instead")

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("Scalar operands are not allowed, use '*' instead")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("Scalar operands are not allowed, use '*' instead")

    # Check sizes
    try:
        res = np.matmul(np.array(m_a), np.array(m_b))
    except ValueError:
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    return res.tolist()


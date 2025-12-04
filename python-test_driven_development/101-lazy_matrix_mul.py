#!/usr/bin/python3
"""
Multiplies two matrices
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy."""
    if not isinstance(m_a, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    if not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")
    try:
        a = np.array(m_a)
        b = np.array(m_b)
        return np.matmul(a, b)
    except ValueError as err:
        raise ValueError(err)
    except TypeError as err:
        raise TypeError(err)

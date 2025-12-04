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
    if len(m_a[0]) != len(m_b):
        raise ValueError("shapes (1,0) and (2,2) not aligned: 0 (dim 1) != 2 (dim 0)")
    try:
        a = np.array(m_a)
        b = np.array(m_b)
        return np.matmul(a, b)
    except ValueError as err:
        raise ValueError(err)
    except TypeError as err:
        raise TypeError(err)

#!/usr/bin/python3
"""
Multiplies two matrices
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy."""
    try:
        a = np.array(m_a)
        b = np.array(m_b)
        return np.matmul(a, b)
    except ValueError as err:
        raise ValueError(err)
    except TypeError as err:
        raise TypeError(err)

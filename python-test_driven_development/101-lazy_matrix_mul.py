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
    rows_a = len(m_a)
    cols_a = len(m_a[0])
    rows_b = len(m_b)
    cols_b = len(m_b[0])

    if cols_a != rows_b:
        raise ValueError(
            f"shapes ({rows_a},{cols_a}) and ({rows_b},{cols_b}) not aligned: "
            f"{cols_a} (dim 1) != {rows_b} (dim 0)"
        )

    if cols_b != rows_a:
        raise ValueError(
            f"shapes ({rows_b},{cols_b}) and ({rows_a},{cols_a}) not aligned: "
            f"{cols_b} (dim 1) != {rows_a} (dim 0)"
        )
    for row in m_a:
    for ele in row:
        if not isinstance(ele, (int, float)):
            raise TypeError("invalid data type for einsum")

    for row in m_b:
    for ele in row:
        if not isinstance(ele, (int, float)):
            raise TypeError("invalid data type for einsum")
    try:
        a = np.array(m_a)
        b = np.array(m_b)
        return np.matmul(a, b)
    except ValueError as err:
        raise ValueError(err)
    except TypeError as err:
        raise TypeError(err)

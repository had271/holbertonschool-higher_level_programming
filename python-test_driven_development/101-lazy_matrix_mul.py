#!/usr/bin/python3
"""
Multiplies two matrices
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy."""

    # scalar check
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    try:
        a = np.array(m_a)
        b = np.array(m_b)

        # attempt multiplication
        return np.matmul(a, b)

    except ValueError as err:
        # dimension mismatch: shapes info موجود داخل err
        msg = str(err)
        if "shapes" in msg:
            raise ValueError(msg)
        if "setting an array element with a sequence" in msg:
            raise ValueError("setting an array element with a sequence.")
        else:
            raise ValueError(msg)

    except TypeError as err:
        # wrong type inside matrix
        msg = str(err)
        if "data type" in msg or "numpy" in msg:
            raise TypeError("invalid data type for einsum")
        else:
            raise TypeError(msg)


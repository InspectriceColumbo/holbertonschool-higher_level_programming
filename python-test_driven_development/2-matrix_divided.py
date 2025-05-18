#!/usr/bin/python3
"""
    Divides all elements of a matrix by a given number.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if rows are not of the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): A matrix (list of lists) of integers/floats.
        div (int/float): The divisor.

    Raises:
        TypeError: If matrix is not a valid matrix.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.

    Returns:
        list: A new matrix with each element divided by div,
              rounded to 2 decimal places.
    """
    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(
        isinstance(el, (int, float)) for row in matrix for el in row
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create a new matrix with rounded division results
    return [[round(el / div, 2) for el in row] for row in matrix]

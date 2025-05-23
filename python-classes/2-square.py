#!/usr/bin/python3
"""
This module defines a basic Square class.
"""


class Square:
    """
    This class represents a geometric square with a given size.
    """
    def __init__(self, size=0):
        """
        Initializes the square with an optional size (0 by default).

        Arguments:
            size (int): The size of the square's side.

        Errors:
            TypeError: Raised if size is not an integer.

            ValueError: Raised if size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

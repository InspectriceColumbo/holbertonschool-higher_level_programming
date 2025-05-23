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
        Initializes the square with an optional size.

        Arguments:
                size (int): The size of the square's side.
        """

        self.size = size

    @property
    def size(self):
        """
        Retrieves the square's size.

        Returns:
                int: The side of the square's side.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Initializes the square with an optional size (0 by default).

        Arguments:
            size (int): The square's new size.

        Errors:
            TypeError: Raised if size is not an integer.

            ValueError: Raised if size is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates and returns the square's area.

        Returns:
                int: The square's area (size^2).
        """
        return self.__size ** 2

#!/usr/bin/python3
"""Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """
    Function checking if the object is an instance of the given class,
        or of a class that inherits from it.

    Returns:
        True if the object is an instance of the given class or,
            a class that inherits from it, otherwise False.
    """
    return isinstance(obj, a_class)

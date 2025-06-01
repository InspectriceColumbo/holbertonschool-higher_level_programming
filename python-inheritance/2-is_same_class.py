#!/usr/bin/python3
"""Exact same object."""


def is_same_class(obj, a_class):
    """
    Function checking if an object is,
    exactly an instance of the given class.
    """
    return type(obj) is a_class

#!/usr/bin/python3
"""Defines a function that checks object class."""


def inherits_from(obj, a_class):

    """Checks if the object is inherited from a class."""

    return isinstance(obj, a_class) and type(obj) is not a_class

#!/usr/bin/python3
"""
Defines a Square class with a private size attribute
and getter/setter for controlled access.
"""


class Square:
    def __init__(self, size=0):
        """
        Initialize the square with an optional size
        """
        self.size = size   # setter çağırılır

    @property  # getter
    def size(self):
        """
        Getter: size dəyərini qaytarır
        """
        return self.__size

    @size.setter  # setter
    def size(self, value):
        """
        Setter: size dəyərini yoxlayaraq təyin edir
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        return self.__size ** 2

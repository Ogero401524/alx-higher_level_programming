#!/usr/bin/python3
"""Defines a base model class."""
class Base:
    """Base model.

    This Represents the "base" for all other classes in project 0x0C*.

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor for Base.

        Parameters:
        id (int, optional): Unique identifier. If provided, assign it to
        the instance's `id` attribute.
        If None, increment the class attribute `__nb_objects` and
        assign its value to `id`.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

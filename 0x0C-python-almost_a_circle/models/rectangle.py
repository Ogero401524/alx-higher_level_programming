#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    """
    The `Rectangle` class represents a rectangle and inherits from the `Base`
    class.
    Attributes:
    - __width (int): Private instance attribute for the width of the rectangle.
    - __height (int): Private instance attribute for the height of
    the rectangle.
    - __x (int): Private instance attribute for the x-coordinate of the
    rectangle.
    - __y (int): Private instance attribute for the y-coordinate of the
    rectangle.
    - id (int): Public instance attribute inherited from the `Base` class.

    Methods:
    - __init__(self, width, height, x=0, y=0, id=None): Class constructor.
        - Calls the super class (`Base`) constructor with the provided `id`.
        - Assigns the values of `width`, `height`, `x`, and `y` to the
    respective private attributes.

    Public Getters and Setters:
    - width: Getter and setter for the width attribute.
    - height: Getter and setter for the height attribute.
    - x: Getter and setter for the x attribute.
    - y: Getter and setter for the y attribute.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor for Rectangle.

        Parameters:
        - width (int): Width of the rectangle.
        - height (int): Height of the rectangle.
        - x (int, optional): x-coordinate of the rectangle (default is 0).
        - y (int, optional): y-coordinate of the rectangle (default is 0).
        - id (int, optional): Unique identifier. If provided, passed to the
        super class (`Base`) constructor.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width attribute."""
        self.__width = value

    @property
    def height(self):
        """Getter method for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height attribute."""
        self.__height = value

    @property
    def x(self):
        """Getter method for x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x attribute."""
        self.__x = value

    @property
    def y(self):
        """Getter method for y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y attribute."""
        self.__y = value

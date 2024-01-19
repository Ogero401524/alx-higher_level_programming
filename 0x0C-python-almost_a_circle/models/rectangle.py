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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method for x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x attribute."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method for y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y attribute."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        area method of the Rectangle method and its attributes
        """
        return self.width * self.height
    def display(self):
        """prints the size of a rectangle"""
        for _ in range(self.height):
            print("#" * self.width)

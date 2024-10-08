#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
	"""This class represents a rectangle"""

	def __init__(self, width=0, height=0):
		"""Initializes the Rectangle object

		Args:
			width (int): The width of the rectangle (default is 0).
			height (int): The height of the rectangle (default is 0).

		Raises:
			TypeError: If width or height is not an integer.
			ValueError: If width or height is less than 0.
		"""
		self.width = width
		self.height = height

	@property
	def width(self):
		"""Retrieves the width of the rectangle"""
		return self.__width

	@width.setter
	def width(self, value):
		"""Sets the width of the rectangle

		Args:
			value (int): The width to set.

		Raises:
			TypeError: If width is not an integer.
			ValueError: If width is less than 0.
		"""
		if not isinstance(value, int):
			raise TypeError("width must be an integer")
		if value < 0:
			raise ValueError("width must be >= 0")
		self.__width = value

	@property
	def height(self):
		"""Retrieves the height of the rectangle"""
		return self.__height

	@height.setter
	def height(self, value):
		"""Sets the height of the rectangle

		Args:
			value (int): The height to set.

		Raises:
			TypeError: If height is not an integer.
			ValueError: If height is less than 0.
		"""
		if not isinstance(value, int):
			raise TypeError("height must be an integer")
		if value < 0:
			raise ValueError("height must be >= 0")
		self.__height = value

#!/usr/bin/env python3
# The shebang tells the operating system which interpreter to use to run this file.
# Here, it uses the Python 3 interpreter found in the system PATH.

from abc import ABC, abstractmethod
# Import the abc module (Abstract Base Classes), which allows the creation of abstract classes.
# ABC is the base class used to define an abstract class.
# abstractmethod is a decorator used to indicate that a method must be implemented in subclasses.

import math
# Import the math module, which provides mathematical functions such as pi.


class Shape(ABC):
    # Define a new class called Shape that inherits from ABC.
    # This means Shape is an abstract class and cannot be instantiated directly.

    """
    Abstract base class for shapes.
    """
    # This docstring describes the purpose of the class.
    # Docstrings are enclosed in triple quotes and are used for documentation.

    @abstractmethod
    # The @abstractmethod decorator indicates that the following method
    # must be implemented by all subclasses.

    def area(self):
        # Define a method named area.
        # Methods are functions defined inside a class.
        # self refers to the current instance of the class.

        """
        Abstract method to return the area of the shape.
        """
        # Docstring explaining the purpose of the method.

        pass
        # pass is a statement that does nothing.
        # It is used here because the method has no implementation.

    @abstractmethod
    # Indicates that the perimeter method must also be implemented in subclasses.

    def perimeter(self):
        # Define a method named perimeter.

        """
        Abstract method to return the perimeter of the shape.
        """
        # Docstring explaining the purpose of the method.

        pass
        # pass indicates that the method has no implementation here.


class Circle(Shape):
    # Define a class Circle that inherits from Shape.
    # Circle must implement the abstract methods area and perimeter.

    """
    Circle shape.
    """
    # Docstring describing the Circle class.

    def __init__(self, radius):
        # Special __init__ method called when creating a new instance.
        # radius represents the radius of the circle.

        self.radius = radius
        # Create an instance attribute named radius and assign the given value.

    def area(self):
        # Implement the area method for the Circle class.

        return math.pi * (self.radius ** 2)
        # Calculate the area of the circle.
        # math.pi provides the value of π.
        # self.radius ** 2 squares the radius.

    def perimeter(self):
        # Implement the perimeter method for the Circle class.

        return 2 * math.pi * self.radius
        # Calculate the perimeter of the circle.
        # Formula: 2 × π × radius.


class Rectangle(Shape):
    # Define a class Rectangle that inherits from Shape.

    """
    Rectangle shape.
    """
    # Docstring describing the Rectangle class.

    def __init__(self, width, height):
        # Special __init__ method called when creating a new instance.
        # width represents the width of the rectangle.
        # height represents the height of the rectangle.

        self.width = width
        # Create an instance attribute named width.

        self.height = height
        # Create an instance attribute named height.

    def area(self):
        # Implement the area method for the Rectangle class.

        return self.width * self.height
        # Calculate the area of the rectangle by multiplying width and height.

    def perimeter(self):
        # Implement the perimeter method for the Rectangle class.

        return 2 * (self.width + self.height)
        # Calculate the perimeter of the rectangle.
        # Formula: 2 × (width + height).


def shape_info(shape):
    # Define a function named shape_info.
    # shape is expected to be an object that has area and perimeter methods.

    """
    Prints the area and perimeter of a shape.
    """
    # Docstring explaining the purpose of the function.

    print(f"Area: {shape.area()}")
    # Print the area of the shape using an f-string.
    # shape.area() is called and its result is inserted into the string.

    print(f"Perimeter: {shape.perimeter()}")
    # Print the perimeter of the shape using an f-string.


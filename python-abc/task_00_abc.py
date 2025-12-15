#!/usr/bin/python3
"""
This module defines an abstract Animal class
and its subclasses Dog and Cat.
"""

# Import the ABC (Abstract Base Class) class and the abstractmethod decorator
# from Python's abc module. These tools are used to create abstract classes,
# which act as templates that other classes must follow.
from abc import ABC, abstractmethod


# Define a class called Animal that inherits from ABC.
# This means Animal is an abstract class and cannot be instantiated directly.
class Animal(ABC):
    """Abstract base class representing an animal."""

    # Use the @abstractmethod decorator to indicate that the sound method
    # must be implemented by all subclasses.
    # An abstract method has no implementation here and only defines a template.
    @abstractmethod
    def sound(self):
        # This method must be overridden in each subclass.
        # The pass keyword indicates that the method does nothing here.
        pass


# Define a class Dog that inherits from the Animal class.
# This means Dog is a type of Animal and must implement the sound method.
class Dog(Animal):
    """Dog class, subclass of Animal."""

    # Override the sound method for the Dog class.
    # This method returns the string "Bark".
    def sound(self):
        """Return the sound made by a dog."""
        return "Bark"


# Define a class Cat that also inherits from the Animal class.
# Cat must also implement the sound method.
class Cat(Animal):
    """Cat class, subclass of Animal."""

    # Override the sound method for the Cat class.
    # This method returns the string "Meow".
    def sound(self):
        """Return the sound made by a cat."""
        return "Meow"

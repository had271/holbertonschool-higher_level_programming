#!/usr/bin/env python3
"""
Custom object serialization using pickle
"""

import pickle


class CustomObject:
    """
    CustomObject class for demonstrating pickle serialization
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object to a file using pickle

        Args:
            filename (str): File to save the serialized object
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (FileNotFoundError, PermissionError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a pickle file

        Args:
            filename (str): File containing the serialized object

        Returns:
            CustomObject or None
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                return obj
        except (FileNotFoundError, PermissionError, EOFError, pickle.PickleError):
            return None

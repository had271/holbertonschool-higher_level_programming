#!/usr/bin/python3
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        for i in self:
            if not isinstance(i, int):
                raise TypeError("unorderable types: str() < int()")
        print(sorted(self))

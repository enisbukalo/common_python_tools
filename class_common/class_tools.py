"""
This module provides classes and functions for working with Python classes.

Classes:
    Singleton: A singleton class that provides a single instance of a class.

Functions:
    None
"""

class Singleton:
    """
    A singleton class that provides a single instance of a class.

    This class ensures that only one instance of a class is created, and provides a way to access that instance.

    Methods:
        __new__(cls): Create and return a singleton instance of the class.
        __init__(self) -> None: Initialize the singleton instance.

    """
    def __new__(cls):
        """
        Create and return a singleton instance of the class.

        This method is called when an instance of the class is created. It checks if the class
        already has an instance. If it does, it returns the existing instance. If it doesn't,
        it creates a new instance and calls the setup method.

        Parameters:
            cls (class): The class object.

        Returns:
            object: The singleton instance of the class.
        """
        if not hasattr(cls, "instance"):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        #NOTE: Just an example of an init within Singleton.
        self.x = 10
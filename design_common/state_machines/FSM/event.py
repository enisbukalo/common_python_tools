from __future__ import annotations

from typing import Any


class Event:
    def __init__(self, data: Any = None) -> None:
        """
        Event class to be used within a Finite State Machine.

        Parameters:
            data (Any): The data to initialize the object with.

        Returns:
            None
        """
        self._data = data

    @property
    def data(self) -> Any:
        """
        Return the value of the data attribute.

        Returns:
            Any: The value of the data attribute.
        """
        return self._data

    @data.setter
    def data(self, data: Any) -> Event:
        """
        Setter method for the data attribute.

        Parameters:
            data (Any): The new value for the data attribute.

        Returns:
            Event: The instance of the Event class with the updated data attribute.
        """
        self._data = data
        return self

    def set_data(self, data: Any) -> Event:
        """
        Sets the data for the event.

        Args:
            data (Any): The data to set for the event.

        Returns:
            Event: The Event object with the updated data.
        """
        self._data = data
        return self

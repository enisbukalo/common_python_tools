from abc import ABC


class Event(ABC):
    def __init__(self, name: str = None) -> None:
        """
        Event class to be used in a Hierarchical State Machine.

        Args:
            name (str, optional): The name of the instance. Defaults to None.

        Raises:
            ValueError: If the name is specified.

        Returns:
            None
        """
        if name is None:
            raise ValueError("name cannot be None")
        self._name = name

    @property
    def name(self) -> str:
        """
        Get the name of the object.

        Returns:
            str: The name of the object.
        """
        return self._name

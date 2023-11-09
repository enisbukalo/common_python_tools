from abc import ABC

from .event import Event


class State(ABC):
    def __init__(self) -> None:
        """
        State class to be used in a Hierarchical State Machine.

        Parameters:
            None

        Returns:
            None
        """
        self._name = self.__class__.__name__.upper()

    @property
    def name(self) -> str:
        """
        Get the name of the object.

        Returns:
            str: The name of the object.
        """
        return self._name

    @classmethod
    def on_enter(self) -> None:
        """
        Handles the actions to be taken when entering the state.

        Parameters:
            None

        Returns:
            None
        """
        print(f"Entering {self.name}")

    @classmethod
    def on_event(self, event: Event):
        """
        Handles the actions to be taken when exiting the state.

        Parameters:
            event (Event): The event to be handled.

        Returns:
            None

        Raises:
            NotImplementedError: This method must be implemented by the child class.
        """
        raise NotImplementedError

    @classmethod
    def on_exit(self) -> None:
        """
        Handles the actions to be taken when exiting the state.

        Parameters:
            None

        Returns:
            None
        """
        print(f"Exiting {self.name}")

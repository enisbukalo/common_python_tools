from abc import ABC
from typing import Self, Union, Iterable

from .event import Event


class State(ABC):
    def __init__(self) -> None:
        """
        State class to be used in a Finite State Machine.

        Parameters:
            None

        Returns:
            None
        """
        self._name = self.__class__.__name__

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
        print(f"Entering {self.name}")

    @classmethod
    def on_event(self, event: Event):
        raise NotImplementedError

    @classmethod
    def on_exit(self) -> None:
        print(f"Exiting {self.name}")

from abc import ABC
from typing import Self, Union, Iterable

from .event import Event


class State(ABC):
    def __init__(self) -> None:
        self._name = self.__repr__

    @property
    def name(self) -> str:
        return self._name

    @classmethod
    def on_enter(self) -> None:
        print(f"Entering {self.__repr__}")

    @classmethod
    def on_event(self, event: Event):
        raise NotImplementedError

    @classmethod
    def on_exit(self) -> None:
        print(f"Exiting {self.__repr__}")

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return self.__class__.__name__

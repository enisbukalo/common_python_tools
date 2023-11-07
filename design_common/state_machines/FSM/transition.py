from abc import ABC
from .state import State


class Transition(ABC):
    def __init__(self, end_state: State = None) -> None:
        if end_state is None:
            raise ValueError("end_state cannot be None")

        self.end_state = end_state

    @classmethod
    def execute(self):
        raise NotImplementedError

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"To{self.__class__.__name__}"

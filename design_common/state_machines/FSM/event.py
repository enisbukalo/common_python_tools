from abc import ABC


class Event(ABC):
    def __init__(self, name: str = None) -> None:
        if name is None:
            raise ValueError("name cannot be None")
        self._name = name

    @property
    def name(self) -> str:
        return self._name

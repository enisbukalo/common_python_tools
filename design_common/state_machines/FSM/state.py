from abc import ABC


class State(ABC):
    def __init__(self) -> None:
        pass

    @classmethod
    def on_enter(self):
        raise NotImplementedError

    @classmethod
    def on_event(self):
        raise NotImplementedError

    @classmethod
    def on_exit(self):
        raise NotImplementedError

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return self.__class__.__name__

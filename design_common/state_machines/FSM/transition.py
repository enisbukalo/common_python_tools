from .event import Event
from .state import State


class Transition:
    def __init__(self, event: Event, from_state: State, to_state: State, callback: callable = None, callback_args=[]) -> None:
        self.event = event
        self.from_state = from_state
        self.to_state = to_state
        self.callback = callback
        self.callback_args = callback_args

    def execute_callback(self) -> None:
        self.callback(*self.callback_args)

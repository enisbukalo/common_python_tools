from typing import Iterable, Union

from .state import State
from .event import Event


class FsmStateMachine:
    def __init__(self, starting_state: State = None) -> None:
        if starting_state is None:
            raise ValueError("starting_state cannot be None")

        self.states: dict[str, State] = {}
        self._current_state: State = starting_state

    @property
    def current_state(self) -> State:
        return self._current_state

    def on_event(self, event: Event) -> None:
        resulting_state: State = self._current_state.on_event(event)
        if resulting_state != self._current_state:
            self._current_state.on_exit()
            self._current_state = resulting_state
            self._current_state.on_enter()

from .state import State
from .transition import Transition


class FsmStateMachine:
    def __init__(self, starting_state: State = None) -> None:
        if starting_state is None:
            raise ValueError("starting_state cannot be None")

        self.transitions = {}
        self.states = {}
        self.current_state = starting_state
        self.previous_state: State = None
        self.transition: Transition = None

    def add_state(self, state: State) -> None:
        self.states[state.__repr__()] = state

    def add_transition(self, transition: Transition) -> None:
        self.transitions[transition.__repr__()] = transition

    def set_state(self, state: State) -> None:
        self.previous_state = self.current_state
        self.current_state = self.states.get(state.__repr__())

    def execute(self) -> None:
        self.current_state.on_exit()
        self.transition.execute()
        self.set_state(self.transition.end_state)
        self.current_state.on_enter()
        self.current_state.on_event()

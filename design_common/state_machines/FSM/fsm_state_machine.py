from .fsm_states import *


class FsmStateMachine:
    def __init__(self) -> None:
        self.handlers = {}
        self.state = StateOne()
        self.end_states = []

    def on_event(self, event):
        self.state = self.state.on_event(event)

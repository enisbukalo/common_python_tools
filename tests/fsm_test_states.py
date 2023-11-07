from design_common.state_machines.FSM.state import State
from test_fsm_events import *


class StartingState(State):
    def __init__(self) -> None:
        super().__init__()

    def on_event(self, event: Event) -> None:
        match event.name:
            case event_one.name:
                return StateOne()


class StateOne(State):
    def __init__(self) -> None:
        super().__init__()

    def on_event(self, event: Event) -> None:
        match event.name:
            case event_two.name:
                return StateTwo()


class StateTwo(State):
    def __init__(self) -> None:
        super().__init__()

    def on_event(self, event: Event) -> None:
        match event.name:
            case event_three.name:
                return EndingState()


class EndingState(State):
    def __init__(self) -> None:
        super().__init__()

    def on_event(self, event: Event) -> None:
        return None

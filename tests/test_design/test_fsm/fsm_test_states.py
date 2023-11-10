from design_common.state_machines.FSM.state import State
from design_common.state_machines.FSM.event import Event

from fsm_test_events import *


class StartingState(State):
    def __init__(self) -> None:
        super().__init__()

    def on_event(self, event: Event):
        match event.name:
            case STARTING_LOGIC.name:
                return None
            case STARTING_EVENT.name:
                return super().on_event(event)
            case _:
                return None


class MiddleState(State):
    def __init__(self) -> None:
        super().__init__()

    def on_event(self, event: Event) -> None:
        match event.name:
            case MIDDLE_LOGIC.name:
                return None
            case ENDING_EVENT.name:
                return super().on_event(event)
            case _:
                return None


class EndingState(State):
    def __init__(self) -> None:
        super().__init__()

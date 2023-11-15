from design_common.state_machines.fsm.state import State
from .fsm_test_events import Events


class StartingState(State):
    def __init__(self) -> None:
        super().__init__()

    def on_event(self, event: int):
        match event:
            case Events.STARTING_LOGIC:
                return None
            case Events.STARTING_EVENT:
                return super().on_event(event)
            case _:
                return None


class MiddleState(State):
    def __init__(self) -> None:
        super().__init__()

    def on_event(self, event: int) -> None:
        match event:
            case Events.MIDDLE_LOGIC:
                return None
            case Events.ENDING_EVENT:
                return super().on_event(event)
            case _:
                return None


class EndingState(State):
    def __init__(self) -> None:
        super().__init__()

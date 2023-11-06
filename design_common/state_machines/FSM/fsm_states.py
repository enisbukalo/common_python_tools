from .state import State
from .events import Events


class StateOne(State):
    def on_event(self, event: Events):
        match event:
            case Events.EVENT_1:
                return StateTwo()
            case _:
                return self


class StateTwo(State):
    def on_event(self, event: Events):
        match event:
            case Events.EVENT_2:
                return StateOne()
            case _:
                return self

from .state import State
from .events import Events


class StateOne(State):
    def on_start(self):
        print("Start StateOne")

    def on_event(self):
        print("Event in StateOne")

    def on_exit(self):
        print("Exit StateOne")


class StateTwo(State):
    def on_start(self):
        print("Start StateTwo")

    def on_event(self):
        print("Event in StateTwo")

    def on_exit(self):
        print("Exit StateTwo")

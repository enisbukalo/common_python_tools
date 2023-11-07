from design_common.state_machines.FSM.state import State


class StartingState(State):
    def on_start(self):
        print(f"Entering {self.__repr__()}")

    def on_event(self):
        print(f"Event in {self.__repr__()}")

    def on_exit(self):
        print(f"Exiting {self.__repr__()}")


class StateOne(State):
    def on_start(self):
        print(f"Entering {self.__repr__()}")

    def on_event(self):
        print(f"Event in {self.__repr__()}")

    def on_exit(self):
        print(f"Exiting {self.__repr__()}")


class StateTwo(State):
    def on_start(self):
        print(f"Entering {self.__repr__()}")

    def on_event(self):
        print(f"Event in {self.__repr__()}")

    def on_exit(self):
        print(f"Exiting {self.__repr__()}")

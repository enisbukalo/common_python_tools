class StateMachine:
    def __init__(self) -> None:
        self.handlers = {}
        self.start_state = None
        self.end_states = []

    def add_state(self, state_name: str, handler: callable, end_state: int = 0) -> None:
        self.handlers[state_name] = handler
        self.end_states.append(state_name)

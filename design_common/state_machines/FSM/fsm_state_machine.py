from .state import State


class FsmStateMachine:
    def __init__(self, starting_state: State = None) -> None:
        """
        Finite State Machine class for keeping track of current state of a system.

        Args:
            starting_state (State, optional): The starting state of the instance. Defaults to None.

        Raises:
            ValueError: If starting_state is None.

        Returns:
            None
        """
        if starting_state is None:
            raise ValueError("starting_state cannot be None")

        self.states: dict[str, State] = {}
        self._current_state: State = starting_state

    @property
    def current_state(self) -> State:
        """
        Get the current state of the object.

        Returns:
            State: The current state of the object.
        """
        return self._current_state

    def on_event(self, event: int) -> None:
        """
        Handle an event and transition to a new state if necessary.

        Args:
            event (int): The event to be handled.

        Returns:
            None
        """
        resulting_state: State = self._current_state.on_event(event)
        if resulting_state is not None and resulting_state != self._current_state:
            self._current_state.on_exit()
            self._current_state = resulting_state
            self._current_state.on_enter()

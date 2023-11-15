from .state import State
from .event import Event


class Transition:
    def __init__(self, event: Event, from_state: State, to_state: State, callback: callable = None, callback_args=[]) -> None:
        """
        Initializes a new instance of the class for creating Transitions between states.

        Args:
            event (Event): The event that triggers the transition.
            from_state (State): The state from which the transition occurs.
            to_state (State): The state to which the transition occurs.
            callback (callable, optional): A callback function to execute after the transition. Defaults to None.
            callback_args (list, optional): Arguments to pass to the callback function. Defaults to [].
        """
        self.event = event
        self.from_state = from_state
        self.to_state = to_state
        self.callback = callback
        self.callback_args = callback_args

    def execute_callback(self) -> None:
        """
        Executes the callback function with the provided arguments and returns the result.

        Returns:
            None
        """
        self.callback(*self.callback_args)

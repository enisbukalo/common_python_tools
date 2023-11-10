from __future__ import annotations
import typing

if typing.TYPE_CHECKING:
    from .transition import Transition

from typing import Union
from .event import Event


class State:
    def __init__(self) -> None:
        """
        State class to be used in a Finite State Machine.

        Parameters:
            None

        Returns:
            None
        """
        self.transitions = []
        self._name = self.__class__.__name__.upper()

    @property
    def name(self) -> str:
        """
        Get the name of the object.

        Returns:
            str: The name of the object.
        """
        return self._name

    def add_transitions(self, transitions: list[Transition]) -> None:
        """
        Add transitions to the list of transitions.

        Args:
            transitions (list): The list of transitions to be added.

        Returns:
            None
        """
        self.transitions.extend(transitions)

    def on_enter(self) -> None:
        """
        Handles the actions to be taken when entering the state.

        Parameters:
            None

        Returns:
            None
        """
        print(f"Entering {self._name}")

    def on_event(self, event: Event) -> Union[Transition, None]:
        """
        Executes the appropriate transition based on the given event.
        Executes transition callback in the process.

        Parameters:
            event (Event): The event triggering the transition.

        Returns:
            Union[Transition, None]: The resulting transition or None if no transition is found.
        """
        transitions_found = [i for i in self.transitions if i.event == event]
        transition: Transition = transitions_found[0] if len(transitions_found) != 0 else None

        if transition is None:
            return None
        else:
            if transition.from_state.name != self._name:
                return None
            else:
                transition.execute_callback()
                return transition.to_state

    def on_exit(self) -> None:
        """
        Handles the actions to be taken when exiting the state.

        Parameters:
            None

        Returns:
            None
        """
        print(f"Exiting {self._name}")

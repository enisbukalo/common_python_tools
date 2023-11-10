from design_common.state_machines.FSM.fsm_state_machine import FsmStateMachine
from design_common.state_machines.FSM.transition import Transition
from design_common.state_machines.FSM.event import Event

from fsm_test_states import *

STARTING_EVENT = Event("event_one")
ENDING_EVENT = Event("event_two")
RESET_EVENT = Event("to_start")


class FsmTestStateMachine(FsmStateMachine):
    def __init__(self) -> None:
        starting_state = StartingState()
        super().__init__(starting_state)

        middle_state = MiddleState()
        ending_state = EndingState()

        starting_transition = Transition(STARTING_EVENT, starting_state, middle_state, callback_to_test, [1, 2, 3])
        middle_transition = Transition(ENDING_EVENT, middle_state, ending_state, callback_to_test, ["CHECK"])
        reset_transition = Transition(RESET_EVENT, ending_state, starting_state, callback_to_test, ["Back", "To", "Start", 1])

        starting_state.add_transitions([starting_transition])
        middle_state.add_transitions([middle_transition])
        ending_state.add_transitions([reset_transition])


def callback_to_test(*args):
    print(f"CALLBACK ARGUMENTS: {args}")


def test_state_machine():
    state_machine = FsmTestStateMachine()

    assert isinstance(state_machine.current_state, StartingState)

    state_machine.on_event(STARTING_EVENT)
    assert isinstance(state_machine.current_state, MiddleState)

    state_machine.on_event(ENDING_EVENT)
    assert isinstance(state_machine.current_state, EndingState)

    state_machine.on_event(RESET_EVENT)
    assert isinstance(state_machine.current_state, StartingState)

    state_machine.on_event(RESET_EVENT)
    assert isinstance(state_machine.current_state, StartingState)

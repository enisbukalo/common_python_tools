from design_common.state_machines.FSM.fsm_state_machine import FsmStateMachine
from design_common.state_machines.FSM.transition import Transition
from design_common.state_machines.FSM.event import Event

from fsm_test_states import *

STARTING_EVENT = Event("event_one")
ENDING_EVENT = Event("event_two")


def callback_to_test(*args):
    print(f"CALLBACK ARGUMENTS: {args}")


def test_state_machine():
    starting_state = StartingState()
    middle_state = MiddleState()
    ending_state = EndingState()

    starting_transition = Transition(STARTING_EVENT, starting_state, middle_state, callback_to_test, [1, 2, 3])
    middle_transition = Transition(ENDING_EVENT, middle_state, ending_state, callback_to_test, ["CHECK"])

    starting_state.add_transitions([starting_transition])
    middle_state.add_transitions([middle_transition])

    state_machine = FsmStateMachine(starting_state)

    assert isinstance(state_machine.current_state, StartingState)

    state_machine.on_event(STARTING_EVENT)
    assert isinstance(state_machine.current_state, MiddleState)

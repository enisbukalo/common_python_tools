from design_common.state_machines.FSM.fsm_state_machine import FsmStateMachine
from design_common.state_machines.FSM.events import Events

from fsm_test_states import *
from fsm_test_transitions import *


def test_state_machine():
    state_machine = FsmStateMachine(StartingState)
    state_machine.add_states([StateOne, StateTwo])
    state_machine.add_transitions(to_one, to_two)

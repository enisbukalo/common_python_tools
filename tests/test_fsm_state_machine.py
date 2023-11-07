from design_common.state_machines.FSM.fsm_state_machine import FsmStateMachine

from fsm_test_states import *


def test_state_machine():
    state_machine = FsmStateMachine(StartingState())

    assert isinstance(state_machine.current_state, StartingState)

    state_machine.on_event(event_one)
    assert isinstance(state_machine.current_state, StateOne)

    state_machine.on_event(event_two)
    assert isinstance(state_machine.current_state, StateTwo)

    state_machine.on_event(event_three)
    assert isinstance(state_machine.current_state, EndingState)

    state_machine.on_event(event_one)
    assert isinstance(state_machine.current_state, EndingState)

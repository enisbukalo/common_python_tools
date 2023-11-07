from design_common.state_machines.FSM.fsm_state_machine import FsmStateMachine
from design_common.state_machines.FSM.events import Events
from design_common.state_machines.FSM.fsm_states import *


def test_state_machine():
    state_machine = FsmStateMachine()

    assert state_machine.state.__str__() == StateOne().__str__()
    state_machine.on_event(Events.EVENT_1)
    assert state_machine.state.__str__() == StateTwo().__str__()
    state_machine.on_event(Events.EVENT_2)
    assert state_machine.state.__str__() == StateOne().__str__()
    state_machine.on_event(Events.EVENT_2)
    assert state_machine.state.__str__() == StateOne().__str__()
    state_machine.on_event(Events.EVENT_1)
    assert state_machine.state.__str__() == StateTwo().__str__()

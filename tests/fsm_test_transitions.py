from design_common.state_machines.FSM.transition import Transition
from fsm_test_states import *

to_one = Transition(StartingState, StateOne)
to_two = Transition(StateOne, StateTwo)

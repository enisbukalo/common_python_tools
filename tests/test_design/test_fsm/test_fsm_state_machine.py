from design_common.state_machines.FSM.fsm_state_machine import FsmStateMachine
from design_common.state_machines.FSM.transition import Transition

from fsm_test_states import *
from fsm_test_events import Events


class FsmTestStateMachine(FsmStateMachine):
    def __init__(self) -> None:
        starting_state = StartingState()
        super().__init__(starting_state)

        middle_state = MiddleState()
        ending_state = EndingState()

        Events.STARTING_LOGIC.data = 10

        starting_logic_transition = Transition(Events.STARTING_LOGIC.set_data(10), starting_state, None, None)
        starting_transition = Transition(Events.STARTING_EVENT, starting_state, middle_state, callback_to_test, [1, 2, 3])
        middle_work_transition = Transition(Events.MIDDLE_LOGIC.set_data(20), middle_state, None, None)
        middle_transition = Transition(Events.ENDING_EVENT, middle_state, ending_state, callback_to_test, ["CHECK"])
        reset_transition = Transition(
            Events.RESET_EVENT, ending_state, starting_state, callback_to_test, ["Back", "To", "Start", 1]
        )

        starting_state.add_transitions([starting_logic_transition, starting_transition])
        middle_state.add_transitions([middle_work_transition, middle_transition])
        ending_state.add_transitions([reset_transition])


def callback_to_test(*args):
    print(f"CALLBACK ARGUMENTS: {args}")


def test_state_machine():
    state_machine = FsmTestStateMachine()

    assert isinstance(state_machine.current_state, StartingState)

    state_machine.on_event(Events.STARTING_LOGIC)
    assert isinstance(state_machine.current_state, StartingState)
    assert Events.STARTING_LOGIC.data == 10

    state_machine.on_event(Events.STARTING_EVENT)
    assert isinstance(state_machine.current_state, MiddleState)

    state_machine.on_event(Events.MIDDLE_LOGIC)
    assert isinstance(state_machine.current_state, MiddleState)
    assert Events.MIDDLE_LOGIC.data == 20

    state_machine.on_event(Events.ENDING_EVENT)
    assert isinstance(state_machine.current_state, EndingState)

    state_machine.on_event(Events.RESET_EVENT)
    assert isinstance(state_machine.current_state, StartingState)

    state_machine.on_event(Events.RESET_EVENT)
    assert isinstance(state_machine.current_state, StartingState)

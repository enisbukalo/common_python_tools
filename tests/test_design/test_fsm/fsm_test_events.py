from design_common.state_machines.FSM.event import Event

STARTING_LOGIC = Event("starting_logic_event")
STARTING_EVENT = Event("event_one")
MIDDLE_LOGIC = Event("middle_logic_event")
ENDING_EVENT = Event("event_two")
RESET_EVENT = Event("to_start")

from enum import Enum


class Events(Enum):
    STARTING_LOGIC = 0
    STARTING_EVENT = 1
    MIDDLE_LOGIC = 2
    ENDING_EVENT = 3
    RESET_EVENT = 4

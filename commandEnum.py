from enum import Enum


class MoveType(Enum):
    RIGHT = 1
    LEFT = 2
    FORWARD = 3
    BACKWARD = 4
    DELIVER = 5
    UNSTUCK = 6
    START_CONVEYER = 7

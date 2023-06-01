# Golle
# This file is made to be a middleman between the main and the image recognition.
# This mena that every time the robot needs a move it calls find move.
import commandEnum


# Class that encapsulates the move into a type and the potential argument that it comes with
# Here speed is only speed
# Argument can be an angle or time
class MoveClass:
    def __init__(self, my_type, my_speed, my_argument):
        self.my_type = my_type
        self.speed = my_speed
        self.argument = my_argument

    def print(self):
        print("Move is: " + str(self.my_type.value) + " amount is: " + str(self.speed))


# The move function that for now just returns right and 500

def find_move() -> MoveClass:
    move = MoveClass(commandEnum.MoveType.RIGHT, 500, 100)
    move.print()
    return move


find_move()

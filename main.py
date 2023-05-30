#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from threading import Thread
import sys

# from robotInfo import GameInfo

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


import socket

# Create your objects here.
ev3 = EV3Brick()
left_wheel_motor = Motor(Port.A)
right_wheel_motor = Motor(Port.B)
convey_motor = Motor(Port.C)
ramp_motor = Motor(Port.D)










# method to make both wheels drive.
# convey_motor.run_angle(700,30000,wait=False)
# robot = DriveBase(left_wheel_motor, right_wheel_motor, wheel_diameter=55.5, axle_track=104)

def main():
    next_move = MoveFinder.find_move()
    match next_move.my_type:
        case commandEnum.MoveType.RIGHT:
            robotTurnRight(next_move.speed, next_move.argument)
        case commandEnum.MoveType.LEFT:
            robotTurnLeft(next_move.speed, next_move.argument)
        case commandEnum.MoveType.START_CONVEYER:
            collectBalls(next_move.argument)
        case commandEnum.MoveType.DELIVER:
            openCloseHatch()
        case commandEnum.MoveType.BACKWARD:
            moveBackward(next_move.speed, next_move.argument)
        case commandEnum.MoveType.FORWARD:
            moveForward(next_move.speed, next_move.argument)
        case commandEnum.MoveType.UNSTUCK:
            unstuckBall()

    print("The game has started")


# robotTurnRight(200, 175, left_wheel_motor, right_wheel_motor) is equal to a 90 degrees right turn
def robotTurnRight(speed, ang):
    left_wheel_motor.run_angle(speed, ang, wait=False)
    right_wheel_motor.run_angle(speed, -ang)

# a TurnLeft(200, 800) is equal to 180 degrees left turn
def turnLeft(speed, ang):
    left_wheel_motor.run_angle(speed, -ang, wait=False)
    right_wheel_motor.run_angle(speed, ang)

# method to move forwards
def moveForward(speed, dist):
   left_wheel_motor.run_angle(speed, dist, wait=False)
   right_wheel_motor.run_angle(speed, dist)

# method to move backwards
def moveBackward(speed, distance):
    right_wheel_motor.run_angle(speed, -distance, wait=False)
    left_wheel_motor.run_angle(speed, -distance)

# make ramp open and clsoe at good speed and angle
def openCloseHatch():
    ramp_motor.run_target(300, 100)
    wait(2000)
    ramp_motor.run_target(250, -90)

# collecting the balls at a good speed for a given time
def collectBalls(time):
    convey_motor.run_target(700, time, wait=False)

# remove stuck balls if there is any
def unstuckBall():
    convey_motor.run_target(200, -1000)

# Write your program here.
ev3.speaker.beep()

# Start the program
collectBalls(10000)
# moveBackward(600, 200)
# turnRight(200, 175)
moveForward(600, 3000)
turnLeft(200, 900)
moveForward(600, 2500)
turnRight(200, 850)
moveBackward(600, 500)
openCloseHatch()



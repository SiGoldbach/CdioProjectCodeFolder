#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from robotInfo import GameInfo
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.

Game1 = GameInfo()
ev3 = EV3Brick()
left_wheel_motor = Motor(Port.A)
right_wheel_motor = Motor(Port.B)
convey_motor = Motor(Port.C)
ramp_motor = Motor(Port.D)

gameWon = 0
def playGame():
    if gameWon == 0:

        if Game1.ballsRemaining == 0:
            # moving to small goal
            Game1.robotLocation = Game1.goalLocationSmall
            #  do: unload function
            Game1.ballsDelivered = Game1.ballsCollected
            gameWon = 1
        else:
            i = 0
        for i in Game1.ballsLocation:
        # nextMove = robotLocation-ballsLocation[i]
            dx = x-xr
            xy = y-yr
            if xd < 0 and yx <0
                turn.move.face(x)
                robot.move.forward(dx)
                turn.move.face(y)
                robot.move.forward(xy)

# method to make both wheels drive.
# convey_motor.run_angle(700,30000,wait=False)
# robot = DriveBase(left_wheel_motor, right_wheel_motor, wheel_diameter=55.5, axle_track=104)


# robotTurnRight(200, 175, left_wheel_motor, right_wheel_motor) is equal to a 90 degrees right turn
def robotTurnRight(speed, ang):
    left_wheel_motor.run_angle(speed, ang, wait=False)
    right_wheel_motor.run_angle(speed, -ang)

# a robotTurnLeft(200, 165, left_wheel_motor, right_wheel_motor) is equal to 90 degrees left turn
def robotTurnLeft(speed, ang):
    left_wheel_motor.run_angle(speed, -ang, wait=False)
    right_wheel_motor.run_angle(speed, ang)

# method to move forwards
def moveForward(speed, ang):
   left_wheel_motor.run_angle(speed, ang, wait=False)
   right_wheel_motor.run_angle(speed, ang)

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
    convey_motor.run_target(700, time)

# remove stuck balls if there is any
def unstuckBall():
    convey_motor.run_target(200, -1000)

#Write your program here.
ev3.speaker.beep()
# moveBackward(Game1.x, 1000)
# robot.straight(1000)
# robot.straight(-1000)
# openCloseHatch()

# moveForward(200, 1000)

# for i in range(4):
   # wait(1500)
    # robotTurnRight(200, 175)
    # wait(1500)
    # robotTurnLeft(200, 163)
  #  wait(1500)
# convey motor decent speed
# convey_motor.run_target(700, 3000)

# this is a good motor-speed for the delivering of balls
# ramp_motor.run_target(300, 100)

# the wait function in milliseconds. 
# wait(3000)

# convey_motor.run_target(700,300000)
# moveBackward(250, 300)
# robotTurnRight(200, 340)
# moveForward(350, 1000)
# robotTurnLeft(200, 370)
# moveForward(250, 1000)
# robotTurnRight(200, 350)
# openCloseHatch()




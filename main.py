#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
left_wheel_motor = Motor(Port.A)
right_wheel_motor = Motor(Port.B)
convey_motor = Motor(Port.C)
ramp_motor = Motor(Port.D)

# 
robot = DriveBase(left_wheel_motor, right_wheel_motor, wheel_diameter=55.5, axle_track=104)


#Write your program here.
ev3.speaker.beep()

convey_motor.run_target(700,3000)

robot.straight(1000)
robot.straight(-1000)

# convey motor decent speed
# convey_motor.run_target(700, 3000)

# this is a good motor-speed for the delivering of balls
# ramp_motor.run_target(300, 100)

# the wait function in milliseconds. 
# wait(3000)

# make ramp close at good speed and angle
# ramp_motor.run_target(250, -90)





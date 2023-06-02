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
import subprocess
import json
import MoveFinder
import moveOptions
# from robotInfo import GameInfo

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


import socket
import time
# Create your objects here.
ev3 = EV3Brick()
left_wheel_motor = Motor(Port.A)
right_wheel_motor = Motor(Port.B)
convey_motor = Motor(Port.C)
ramp_motor = Motor(Port.D)






# method to make both wheels drive.
# convey_motor.run_angle(700,30000,wait=False)
# robot = DriveBase(left_wheel_motor, right_wheel_motor, wheel_diameter=55.5, axle_track=104)
# robotTurnRight(200, 175, left_wheel_motor, right_wheel_motor) is equal to a 90 degrees right turn
#def robotTurnRight(speed, ang):
 #   left_wheel_motor.run_angle(speed, ang, wait=False)
  #  right_wheel_motor.run_angle(speed, -ang)

# a TurnLeft(200, 800) is equal to 180 degrees left turn
#def turnLeft(speed, ang):
 #   left_wheel_motor.run_angle(speed, -ang, wait=False)
  #  right_wheel_motor.run_angle(speed, ang)

def turn(speed, ang):
    if ang >= 0:
        left_wheel_motor.run_angle(speed, -ang, wait=False)
        right_wheel_motor.run_angle(speed, ang)
    else:
        left_wheel_motor.run_angle(speed, ang, wait=False)
        right_wheel_motor.run_angle(speed, -ang)

# method to move forwards
def moveForward(speed, dist):
   left_wheel_motor.run_angle(speed, dist, wait=False)
   right_wheel_motor.run_angle(speed, dist)

# method to move backwards
def moveBackward(speed, dist):
    right_wheel_motor.run_angle(speed, -dist, wait=False)
    left_wheel_motor.run_angle(speed, -dist)

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

# ev3.speaker.beep()
for i in range(2):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("10.209.192.170", 5000))
    sock.send(b"GET /test HTTP/1.1\r\nHost:10.209.192.170\r\n\r\n")
    response = ''
    while True:
        data = sock.recv(1024)
        if not data:
            break
        response += data.decode('utf-8')
    headers, body = response.split('\r\n\r\n', 1)
    move = json.loads(body, object_hook=MoveFinder.as_payload)
    print(move.toString())
    print("Testing the types should be String int, int")
    print(type(move.type))
    print(type(move.speed))
    print(type(move.argument))
    sock.close()

# Start the program
# collectBalls(10000)
# moveBackward(600, 200)
# turnRight(200, 175)
# turnLeft(200, 800)
# turn(200, 800)
# moveForward(600, 2500)
# turnRight(200, 750)
# turn(200, -750)
# moveBackward(600, 500)
# openCloseHatch()

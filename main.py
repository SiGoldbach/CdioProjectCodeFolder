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
import threading
# from robotInfo import GameInfo

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


import socket
import time
# Create your objects here.
ev3 = EV3Brick()
left_wheel_motor = Motor(Port.A)
right_wheel_motor = Motor(Port.B)
convey_motor = Motor(Port.D)
ramp_motor = Motor(Port.C)
robot = DriveBase(left_wheel_motor,right_wheel_motor,35,170)
#I am here making a motor pair 







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

# method to move forwards
def moveForward(speed, dist):
   robot.drive(speed, 0)
   wait(dist)
   robot.stop()
   

# method to move backwards
def moveBackward(speed, dist):
    right_wheel_motor.run_angle(speed, -dist, wait=False)
    left_wheel_motor.run_angle(speed, -dist)

#Problems there are some problems about the ramp if the ramp closes to much it tries to spin the motor but cant and therefore the thread may get stuck 

# make ramp open and clsoe at good speed and angle
def openCloseHatch():
    ramp_motor.run_target(300, -40)
    print("Openened the ramp")
    wait(2000)
    print("About to close the ramp")
    ramp_motor.run_target(250, 40)
    print("DEBUGGIN")
    print("done using the latch")

# collecting the balls at a good speed for a given time
def collectBalls(time):
    print("Collecting Balls")
    convey_motor.run_angle(700, -time, wait=False)
    print("Done collecting Balls")

# remove stuck balls if there is any
def unstuckBall():
    convey_motor.run_target(200, -1000)
# function for deciding and taking a move. 
def takeMove(move):
    if move.type==moveOptions.FORWARD:
        moveForward(move.speed,move.argument)
    if move.type==moveOptions.BACKWARD:
        moveBackward(move.speed,move.argument)
    if move.type==moveOptions.TURN:
        angleMove(move.argument)
    if move.type==moveOptions.DELIVER:
        openCloseHatch()

def angleMove(angle):
    robot.turn(angle)
def straight(distance):
    robot.straight(distance)
    
def pickUpBallTest():
    angleMove(-7.6)
    
   


    #openCloseHatch()

    
    
# Write your program here.
#I am here starting a thread to take care of the conveyor

#Here the current competition mode for the robot is written 

def belt_test():
    print("Doing the belt test")
    pick_balls_thread=threading.Thread(target = collectBalls(500000))
    pick_balls_thread.start
    time.sleep(2)
    moveForward(500, 1000)
    moveForward(-500, 1000)

    




def comp():
    pick_balls_thread=threading.Thread(target = collectBalls(500000))
    pick_balls_thread.start
    for i in range(1000):
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
        print("Given move is: "+move.toString())
        takeMove(move)
        time.sleep(2)
        sock.close()
        

comp()


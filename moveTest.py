from robotInfo import GameInfo

Game1 = GameInfo()
ev3 = EV3Brick()
left_wheel_motor = Motor(Port.A)
right_wheel_motor = Motor(Port.B)
convey_motor = Motor(Port.C)
ramp_motor = Motor(Port.D)

gameWon = 0

def playGame():
    global gameWon

    if gameWon == 0:

        if Game1.ballsRemaining == 0:
            # moving to small goal
            Game1.robotLocation = Game1.goalLocationSmall
            #  do: unload function
            Game1.ballsDelivered = Game1.ballsCollected
            gameWon = 1
        else:
            for ball_location in Game1.ballsLocation:
                # calculate the distance and angle to the ball
                dx = ball_location[0] - Game1.robotLocation[0]
                dy = ball_location[1] - Game1.robotLocation[1]
                distance = math.sqrt(dx**2 + dy**2)
                angle_degrees = math.degrees(math.atan2(dy, dx))

                # turn towards the ball
                if angle_degrees < 0:
                    robotTurnLeft(200, abs(angle_degrees))
                else:
                    robotTurnRight(200, angle_degrees)

                # move towards the ball
                moveForward(200, distance)

                # pick up the ball
                collectBalls(2000)

                # update the robot's location and balls remaining
                Game1.robotLocation = ball_location
                Game1.ballsRemaining -= 1

def robotTurnRight(speed, angle_degrees):
    angle = angle_degrees / 90 * 175
    left_wheel_motor.run_angle(speed, angle, wait=False)
    right_wheel_motor.run_angle(speed, -angle)

def robotTurnLeft(speed, angle_degrees):
    angle = angle_degrees / 90 * 165
    left_wheel_motor.run_angle(speed, -angle, wait=False)
    right_wheel_motor.run_angle(speed, angle)

def moveForward(speed, distance):
    left_wheel_motor.run_angle(speed, distance, wait=False)
    right_wheel_motor.run_angle(speed, distance)

def collectBalls(time):
    convey_motor.run_target(700, time)

#Write your program here.
ev3.speaker.beep()

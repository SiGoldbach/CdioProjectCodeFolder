import math
import main


# Here we use geometry and the input from camera to find the preferred move. 
# class CalculateMove:


# Find a concentrated area of red pixels that
# ensure that if an obstacle is located in the path of the calculateMove how to handle.
# class AvoidRedPixel:


# Here we manage how many balls are left
# Location of goals.

class GameLogic:
    y, robot_y, ysm, ylm = 0, 0, 0, 0
    x, robot_x, xsm, xlm = 0, 0, 0, 0
    robotLocation = [robot_x, robot_y]
    ballsLocation = [x, y]
    robotStartLocation = [10, 1]
    ballsDelivered = 0
    ballsCollected = 0
    goalLocationSmall = [xsm, ysm]
    goalLocationLarge = [xlm, ylm]
    totalBalls = len(ballsLocation)
    # this is calculating the angle to turn based on what way the robot if facing.
    angle_degrees = (math.atan2(y - robot_y, x - robot_x)) * (180 / math.pi)
    ballsRemaining = int(totalBalls - ballsCollected)
    distanceToMove = math.sqrt((x - robot_x) ^ 2 + (y - robot_y) ^ 2)


# created fake scenario for the robot
Game1 = GameLogic()
y, robot_y, ysm, ylm = 0, 0, 0, 0
x, robot_x, xsm, xlm = 0, 0, 0, 0
Game1.robotStartLocation = [10, 1]
Game1.robotLocation = [robot_x, robot_y]
Game1.ysm = 10
Game1.xsm = 1
Game1.xlm = 20
Game1.ylm = 10
Game1.ballsCollected = 0
Game1.ballsDelivered = 0
Game1.goalLocationSmall = [xsm, ysm]
Game1.goalLocationLarge = [xlm, ylm]
Game1.ballsLocation = [[2, 4], [6, 3], [8, 8], [8, 3], [10, 10], [20, 20], [1, 9], [16, 14]]
Game1.totalBalls = len(Game1.ballsLocation)
Game1.angle_degrees = 54
Game1.distanceToMove = 200
Game1.distanceToGoal = math.sqrt((xsm - robot_x) ^ 2 + (ysm - robot_y) ^ 2)
Game1.angleToGoal = (math.atan2(y - ysm, x - xsm)) * (180 / math.pi)


# Game1.ballsRemaining = int(Game1.totalBalls - Game1.ballsCollected)

def playGame():
    gameWon = 0
    ballsCollected = 0
    ballsRemaining = Game1.totalBalls

    if gameWon == 0:
        main.collectBalls(10000000000)

        if ballsRemaining == 0:
            # moving to small goal
            main.turn(200, Game1.angleToGoal)
            main.moveForward(500, Game1.distanceToGoal)
            #  do: unload function
            main.openCloseHatch()
            ballsDelivered = ballsCollected
            gameWon = 1
        else:
            i = 0
        for i in Game1.ballsLocation:
            # nextMove = robotLocation-ballsLocation[i]
            main.turn(200, Game1.angle_degrees)
            main.moveForward(500, Game1.distanceToMove)
            if i == 6 | 12 | 18 | 24 | 30:
                # moving to small goal
                main.turn(200, Game1.angleToGoal)
                main.moveForward(500, Game1.distanceToGoal)
                # face hatchet towards goal
                main.turn(200, 180)
                #  do: unload function
                main.openCloseHatch()

    ballsCollected += 1
    ballsRemaining = Game1.totalBalls - ballsCollected


if gameWon == 1:
    print("we did it")
    # play winner music

coordinates_array = [[2, 4], [6, 3], [8, 8], [8, 3], [10, 10], [20, 20], [1, 9], [16, 14]]


def find_nearest_ball(robot_x, robot_y, coordinates_array):
    closest_distance = float('inf')
    closest_coordinates = []

    for coordinates in coordinates_array:
        x = coordinates[0]
        y = coordinates[1]
        distance = math.sqrt((x - robot_x) ** 2 + (y - robot_y) ** 2)

        if distance < closest_distance:
            closest_distance = distance
            closest_coordinates = coordinates

    return closest_coordinates, closest_distance

def calculate_angle(target_x, target_y, robot_x, robot_y):
    angle = math.atan2(target_y - robot_y, target_x - robot_x) * (180 / math.pi)
    return angle

def move_robot(target_x, target_y):
    global robot_x, robot_y
    robot_x = target_x
    robot_y = target_y
    # Implement your code to move the robot to the target coordinates
    print("Moving robot to coordinates:", target_x, target_y)

# Find the closest coordinates and distance
closest_coordinates, closest_distance = find_nearest_ball(robot_x, robot_y, coordinates_array)
print("Closest coordinates:", closest_coordinates)

# Calculate the angle between the robot's start location and the first target
angle = calculate_angle(closest_coordinates[0], closest_coordinates[1], robot_x, robot_y)
print("Angle:", angle)

# Move the robot to the closest coordinates
move_robot(closest_coordinates[0], closest_coordinates[1])

# Print the updated robot's coordinates
print("Robot's coordinates:", robot_x, robot_y)

# Print the closest distance
print("Closest distance:", closest_distance)

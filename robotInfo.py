import math
import main


class GameInfo:
    y, yr, ysm, ylm = 0, 0, 0, 0
    x, xr, xsm, xlm = 200, 0, 0, 0
    robotLocation = [xr, yr]
    ballsLocation = [x, y]
    robotStartLocation = [10, 1]
    ballsDelivered = 0
    ballsCollected = 0
    goalLocationSmall = [xsm, ysm]
    goalLocationLarge = [xlm, ylm]
    totalBalls = len(ballsLocation)
    ballsRemaining = int(totalBalls - ballsCollected)
    main.moveForward()


# created fake scenario for the robot
Game1 = GameInfo()
y, yr, ysm, ylm = 0, 0, 0, 0
x, xr, xsm, xlm = 0, 0, 0, 0
Game1.robotStartLocation = [10, 1]
Game1.robotLocation = [xr, yr]
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
Game1.ballsRemaining = int(Game1.totalBalls - Game1.ballsCollected)

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
            dx = x - xr
            dy = y - yr
            if dx != 0 and dy != 0:
                angle_radian = math.atan2(dx, dy)
                angle_degree = math.degrees(angle_radian)
                # find out how it returns the degree as if we have to turn left or right
                main.robotTurnRight(angle_degree)
                distance_to_move = (math.sqrt((x * x) + (y * y)))
                main.moveForward(500, distance_to_move)

            if dx == 0 and dy != 0:
                angle_radian = math.atan2(dx, dy)
                angle_degree = math.degrees(angle_radian)
                # find out how it returns the degree as if we have to turn left or right
                main.robotTurnRight(angle_degree)
                distance_to_move = (math.sqrt((x * x) + (y * y)))
                main.moveForward(500, distance_to_move)

            if dx != 0 and dy == 0:
                angle_radian = math.atan2(dx, dy)
                angle_degree = math.degrees(angle_radian)
                # find out how it returns the degree as if we have to turn left or right
                main.robotTurnRight(angle_degree)
                distance_to_move = (math.sqrt((x * x) + (y * y)))
                main.moveForward(500, distance_to_move)

    Game1.robotLocation = i
    Game1.ballsCollected += 1


if gameWon == 1:
    print("we did it")
    # play winner music

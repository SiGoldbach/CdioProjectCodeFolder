import math
import subprocess
import sys

import numpy as np
import cv2 as cv
from sympy import symbols, solve

ySize = 480
xSize = 640


# This method takes argument in type of y=mx+b
def find_intersection(a1, b1, a2, b2):
    # Here b is defined to be -1 as the value before the y when putting it on the other side
    solution = [(b2 - b1) / (a1 - a2), 0]
    solution[1] = a1 * solution[0] + b1
    # print(solution)


img = cv.imread('Resources/Pictures/fieldWithBalls.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
img = cv.medianBlur(img, 5)
cimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 20,
                          param1=400, param2=8, minRadius=0, maxRadius=10)
circles = np.uint16(np.around(circles))
print("Amount of circles: " + str(len(circles[0])))
for i in circles[0, :]:
    # draw the outer circle
    cv.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
dst = cv.Canny(img, 0, 200, None, 3)
lines = cv.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)
print(type(lines[0]))
print(lines[0][0][0])
LineEquations = []
if lines is not None:
    for i in range(0, len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = math.cos(theta)
        b = math.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * a))
        pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * a))
        cv.line(cimg, pt1, pt2, (0, 0, 255), 1, cv.LINE_AA)
        # m is slope
        m = (pt1[0] - pt2[0]) / (pt1[1] - pt2[1])
        # now I am finding the b value
        b = symbols('b')
        equation = pt1[0] * m + b - pt1[1]
        bVal = solve(equation)
        yVal = m * pt1[0] + bVal[0]
        betterLineRepresentation = [m, bVal[0]]
        LineEquations.append(betterLineRepresentation)
sys.stdout.flush()
point_try_counter = 0
for i in range(0, len(LineEquations)):
    for j in range(i + 1, len(LineEquations)):
        print(i)
        print(j)
        print(LineEquations[i])
        print(LineEquations[j])
        find_intersection(LineEquations[i][0], LineEquations[i][1], LineEquations[j][0], LineEquations[j][1])
        point_try_counter = point_try_counter + 1
print(point_try_counter)
cv.imshow('detected circles', cimg)
cv.waitKey(0)
cv.destroyAllWindows()
subprocess.run(['python', 'helloWorld.py', 'Very fun argument'])

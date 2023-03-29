import math

import numpy as np
import cv2 as cv

img = cv.imread('Resources/Pictures/fieldWithBalls_concealed.jpg', cv.IMREAD_GRAYSCALE)
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

if lines is not None:
    for i in range(0, len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = math.cos(theta)
        b = math.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
        pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
        cv.line(cimg, pt1, pt2, (0, 0, 255), 1, cv.LINE_AA)
cv.imshow('detected circles', cimg)
cv.waitKey(0)
cv.destroyAllWindows()

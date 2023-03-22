# Sebastian Goldbach
# This file is made with the purpose of taking a picture and mapping what is currently in it

import cv2 as cv
import numpy as np
import time


class Field:
    width = 120
    height = 180
    ball_location = list
    ball_amount = 0


image = cv.imread('Resources/Pictures/withRobot.jpg')
print(image[0][0])
# cv.imshow('Read picture', image)
img_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
blank = np.zeros((480, 640, 3), dtype='uint8')
# blank2 = np.zeros((480, 640, 3), dtype='uint8')

print(image[0][0][2])

lower_red = np.array([170, 50, 180])
upper_red = np.array([180, 255, 255])
# trying to change blank to a better model
start = time.time()
i_counter = 0
j_counter = 0
img_height, img_width, _ = image.shape
red_pixels = 0
white_pixels = 0
maxVal = list

for i in range(img_height):
    for j in range(img_width):
        # detecting walls
        if 155 <= image[i][j][2] <= 255 and 0 <= image[i][j][0] <= 100 and 0 <= image[i][j][1] <= 100:
            red_pixels += 1
            blank[i][j][2] = 255
        if 180 <= image[i][j][0] and 180 <= image[i][j][1] and 180 <= image[i][j][2]:
            white_pixels += 1
            blank[i][j][0] = 255
            blank[i][j][1] = 255
            blank[i][j][2] = 255
# Here I will try to find the four corners by finding extreme red values
end = time.time()
im_gray = cv.cvtColor(blank, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(im_gray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
circles2 = 0
circles_list = []
for cnt in contours:
    approx = cv.approxPolyDP(cnt, .03 * cv.arcLength(cnt, True), True)
    k = cv.isContourConvex(approx)
    if k:
        circles2 += 1
        M = cv.moments(cnt)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        print("Center of this circle should be: " + str(cX) + " " + str(cY))
        cv.circle(blank, (cX, cY), 7, (255, 0, 0), -1)
        circles_list.append([(cX, cY)])
# Now to find the big square
edges = cv.Canny(im_gray, 50, 150, apertureSize=3)
lines = cv.HoughLinesP(
    edges,  # Input edge image
    1,  # Distance resolution in pixels
    np.pi / 180,  # Angle resolution in radians
    threshold=100,  # Min number of votes for valid line
    minLineLength=5,  # Min allowed length of line
    maxLineGap=10  # Max allowed gap between line for joining them
)

lines_list = []
for points in lines:
    # Extracted points nested in the list
    x1, y1, x2, y2 = points[0]
    # Draw the lines joing the points
    # On the original image
    cv.line(blank, (x1, y1), (x2, y2), (0, 255, 0), 2)
    # Maintain a simples lookup list for points
    lines_list.append([(x1, y1), (x2, y2)])

print("Contour length: " + str(len(contours)))
print("Line amount: " + str(len(lines_list)))

timeForTransform = end - start
print('time for transform: ' + str(timeForTransform))
print("Amount of red pixels: " + str(red_pixels))
print("Amount of white pixels: " + str(white_pixels))
print("Amount of circles: " + str(circles2))

cv.imshow('Original', image)
cv.imshow('Obstacles and balls drawn: ', blank)

# cv.imshow('StartModel', blank)
cv.waitKey(0)

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


image = cv.imread('Resources/Pictures/fieldWithBalls.jpg')
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
maxVal = list

for i in range(img_height):
    for j in range(img_width):
        # detecting walls
        if 155 <= image[i][j][2] <= 255 and 0 <= image[i][j][0] <= 100 and 0 <= image[i][j][1] <= 100:
            red_pixels += 1
            blank[i][j][2] = 255
        if 180 <= image[i][j][0] and 180 <= image[i][j][1] and 180 <= image[i][j][2]:
            blank[i][j][0] = 255
            blank[i][j][1] = 255
            blank[i][j][2] = 255
# Here I will try to find the four corners by finding extreme red values

end = time.time()

timeForTransform = end - start
print('time for transform: ' + str(timeForTransform))
print("Amount of red pixels: " + str(red_pixels))
cv.imshow('Original', image)
cv.imshow('BetterModel', blank)

# cv.imshow('StartModel', blank)
cv.waitKey(0)

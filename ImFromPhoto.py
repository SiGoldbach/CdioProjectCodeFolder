import cv2 as cv
import numpy as np
import time

class Field:
    width = 120
    height = 180
    ball_location = list
    ball_amount = 0

image = cv.imread('Resources/Pictures/fieldWithBalls_concealed.jpg')
print(image[0][0])

# Convert the image to grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Create a blank image
blank = np.zeros_like(image)

lower_red = np.array([170, 50, 180])
upper_red = np.array([180, 255, 255])

start = time.time()

red_pixels = 0
white_pixels = 0

img_height, img_width, _ = image.shape

for i in range(img_height):
    for j in range(img_width):
        if 155 <= image[i][j][2] <= 255 and 0 <= image[i][j][0] <= 100 and 0 <= image[i][j][1] <= 100:
            red_pixels += 1
            blank[i][j][2] = 255
        if 180 <= image[i][j][0] and 180 <= image[i][j][1] and 180 <= image[i][j][2]:
            white_pixels += 1
            blank[i][j][0] = 255
            blank[i][j][1] = 255
            blank[i][j][2] = 255

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
        print("Center of this circle should be:", cX, cY)
        cv.circle(blank, (cX, cY), 7, (255, 0, 0), -1)
        circles_list.append([(cX, cY)])

# Adjust the parameters for the HoughLinesP function to improve the line detection
edges = cv.Canny(im_gray, 50, 150, apertureSize=3)
lines = cv.HoughLinesP(
    edges,
    rho=1,
    theta=np.pi / 180,
    threshold=50,  # Adjust this value for line detection sensitivity
    minLineLength=100,  # Adjust this value for the minimum length of lines
    maxLineGap=10  # Adjust this value for the maximum gap between line segments
)

lines_list = []
if lines is not None:
    for points in lines:
        x1, y1, x2, y2 = points[0]
        cv.line(blank, (x1, y1), (x2, y2), (0, 255, 0), 2)
        lines_list.append([(x1, y1), (x2, y2)])

timeForTransform = end - start
print('Time for transform:', timeForTransform)
print("Amount of red pixels:", red_pixels)
print("Amount of white pixels:", white_pixels)
print("Amount of circles:", circles2)

cv.imshow('Original', image)
cv.imshow('Obstacles and balls drawn:', blank)
cv.waitKey(0)
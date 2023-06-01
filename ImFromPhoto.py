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


image = cv.imread('Resources/Pictures/withRobot9.jpg')
if image is None:
    print("No image found")
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
green_pixels = 0
maxVal = list

for i in range(img_height):
    for j in range(img_width):
        # detecting walls

        if image[i][j][0] <= 220 and 40 <= image[i][j][1] <= 100 and 25 <= image[i][j][2] <= 80:
            # Detected green square
            blank[i][j][0] = 0
            blank[i][j][1] = 0
            blank[i][j][2] = 0
            cv.rectangle(blank, (j, i), (j, i), (0, 255, 255), 1)


        if image[i][j][0] <= 120 and 150 <= image[i][j][1] <= 200 and 75 <= image[i][j][2] <= 110:
            # Detected green square
            blank[i][j][0] = 0
            blank[i][j][1] = 0
            blank[i][j][2] = 0
            cv.rectangle(blank, (j, i), (j, i), (255, 255, 255), 1)
            
        if 200 <= image[i][j][2] and 100 >= image[i][j][1]:
            red_pixels += 1
            blank[i][j][2] = 255
        if 190 <= image[i][j][2] and 120 >= image[i][j][0] and 155 <= image[i][j][1]:
            blank[i][j][0] = 0
            blank[i][j][1] = 150
            blank[i][j][2] = 255
        if 200 <= image[i][j][2]:
            red_pixels += 1
            blank[i][j][2] = 255
        if 200 <= image[i][j][0] and 210 <= image[i][j][1] and 210 <= image[i][j][2]:
            white_pixels += 1
            blank[i][j][0] = 255
            blank[i][j][1] = 0
            blank[i][j][2] = 0
            cv.circle(blank, (j,i), 1, (255, 0, 0), -1)

# Here I will try to find the four corners by finding extreme red values
end = time.time()
im_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(im_gray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
circles2 = 0
circles_list = []

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
  
# Blur using 3 * 3 kernel.
gray_blurred = cv.blur(gray, (3, 3))
  
# Apply Hough transform on the blurred image.
detected_circles = cv.HoughCircles(gray_blurred, 
                   cv.HOUGH_GRADIENT, 1, 20, param1 = 60,
               param2 = 20, minRadius = 1, maxRadius = 10)
  
# Draw circles that are detected.
if detected_circles is not None:
  
    # Convert the circle parameters a, b and r to integers.
    detected_circles = np.uint16(np.around(detected_circles))
  
    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]
        circles2 += 1
        # Draw the circumference of the circle.
        cv.circle(blank, (a, b), r, (0, 255, 0), 2)
        print("Center of this circle should be: " + str(a) + " " + str(b))
        # Draw a small circle (of radius 1) to show the center.
        cv.circle(blank, (a, b), 1, (0, 0, 255), 3)

   
#for cnt in contours:
#    approx = cv.approxPolyDP(cnt, 0.1 * cv.arcLength(cnt, True), True)
#   k = cv.isContourConvex(approx)
#    if k:
#        circles2 += 1
#        M = cv.moments(cnt)
#        cX = int(M["m10"] / M["m00"])
#        cY = int(M["m01"] / M["m00"])
#        print("Center of this circle should be: " + str(cX) + " " + str(cY))
#        cv.circle(blank, (cX, cY), 7, (255, 0, 0), -1)
#        circles_list.append([(cX, cY)])


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
if lines is None:
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

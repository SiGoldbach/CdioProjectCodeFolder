import cv2 as cv
import numpy as np
import time

image = cv.imread('Resources/Pictures/withRobot9.jpg')
if image is None:
    print("No image found")
print(image[0][0])

img_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
blank = np.zeros((480, 640, 3), dtype='uint8')

lower_red = np.array([170, 50, 180])
upper_red = np.array([180, 255, 255])

start = time.time()

img_height, img_width, _ = image.shape

red_pixels = np.sum((image[..., 0] <= 220) & (40 <= image[..., 1]) & (25 <= image[..., 2]) &
                    (image[..., 2] <= 80))
green_mask1 = ((image[..., 0] <= 220) & (40 <= image[..., 1]) & (25 <= image[..., 2]) &
               (image[..., 2] <= 80)).astype(np.uint8)
blank[..., :][green_mask1 == 1] = (0, 255, 255)

green_mask2 = ((image[..., 0] <= 120) & (150 <= image[..., 1]) & (75 <= image[..., 2]) &
               (image[..., 2] <= 110)).astype(np.uint8)
blank[..., :][green_mask2 == 1] = (255, 255, 255)

red_mask1 = ((200 <= image[..., 2]) & (100 >= image[..., 1])).astype(np.uint8)
red_pixels += np.sum(red_mask1)
blank[..., 2][red_mask1 == 1] = 255

red_mask2 = ((190 <= image[..., 2]) & (120 >= image[..., 0]) & (155 <= image[..., 1])).astype(np.uint8)
blank[..., 0][red_mask2 == 1] = 0
blank[..., 1][red_mask2 == 1] = 150
blank[..., 2][red_mask2 == 1] = 255

white_mask = ((200 <= image[..., 2]) & (210 <= image[..., 0]) & (210 <= image[..., 1])).astype(np.uint8)
white_pixels = np.sum(white_mask)
blank[..., 0][white_mask == 1] = 255
blank[..., 1][white_mask == 1] = 0
blank[..., 2][white_mask == 1] = 0
blank[..., :][white_mask == 1] = (255, 0, 0)

end = time.time()

gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
gray_blurred = cv.blur(gray, (3, 3))

detected_circles = cv.HoughCircles(
    gray_blurred,
    cv.HOUGH_GRADIENT,
    1,
    20,
    param1=60,
    param2=20,
    minRadius=1,
    maxRadius=10
)

if detected_circles is not None:
    detected_circles = np.uint16(np.around(detected_circles))
    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]
        cv.circle(blank, (a, b), r, (0, 255, 0), 2)
        print("Center of this circle should be: " + str(a) + " " + str(b))
        cv.circle(blank, (a, b), 1, (0, 0, 255), 3)

edges = cv.Canny(gray, 50, 150, apertureSize=3)

lines = cv.HoughLinesP(
    edges,
    1,
    np.pi / 180,
    threshold=100,
    minLineLength=5,
    maxLineGap=10
)

if lines is not None:
    lines = lines.squeeze()
    for x1, y1, x2, y2 in lines:
        cv.line(blank, (x1, y1), (x2, y2), (0, 255, 0), 2)

time_for_transform = end - start

print("Amount of red pixels: " + str(red_pixels))
print("Amount of white pixels: " + str(white_pixels))
print("Amount of circles: " + str(len(detected_circles[0])))

cv.imshow('Original', image)
cv.imshow('Obstacles and balls drawn: ', blank)

print('Time for transform: ' + str(time_for_transform))

cv.waitKey(0)

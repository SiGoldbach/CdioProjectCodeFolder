import numpy as np
import cv2 as cv

img = cv.imread('Resources/Pictures/fieldWithBalls.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
equ = cv.equalizeHist(img)
cv.imwrite('res.png', equ)
ret, thresh = cv.threshold(equ, 127, 255, 0)

contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
circles = cv.HoughCircles(equ, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
if circles is not None:
    print("Amount of circles: " + str(len(circles)))
else:
    print("No circles where found")
# ensure at least some circles were found
circles = np.uint16(np.around(circles))
print("Amount of circles: " + str(len(circles)))
for i in range(len(circles)):
    print("Drawing a circle")
    # draw the outer circle
    cv.circle(equ, (circles[i][0], circles[i][1]), circles[i][2], (0, 255, 0), 2)
    # draw the center of the circle
    cv.circle(equ, (circles[i][0], circles[i][1]), 2, (0, 0, 255), 3)

cv.imwrite('tresh.png', equ)

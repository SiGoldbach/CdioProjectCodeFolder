import cv2
import numpy as np

# Load the image
img = cv2.imread('Resources/Pictures/fieldWithBalls.jpg')

# Convert to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define the range of white color in HSV
lower_white = np.array([0, 0, 200])
upper_white = np.array([180, 30, 255])

# Create a mask for white color
mask_white = cv2.inRange(hsv, lower_white, upper_white)

# Define the range of ping pong ball color in HSV
lower_ball = np.array([10, 25, 25])
upper_ball = np.array([60, 255, 255])

# Create a mask for ping pong ball color
mask_ball = cv2.inRange(hsv, lower_ball, upper_ball)

# Combine the masks
mask = cv2.bitwise_or(mask_white, mask_ball)

# Apply a blur to reduce noise
mask_blur = cv2.GaussianBlur(mask, (5, 5), 0)

# Detect circles using the HoughCircles method
circles = cv2.HoughCircles(mask_blur, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

# Draw circles on the original image
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(img, (x, y), r, (0, 255, 0), 2)

# Display the resulting image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
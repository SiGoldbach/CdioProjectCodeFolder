import cv2 as cv
import numpy as np

# videoCapture = cv.VideoCapture(1, cv.CAP_DSHOW)
# image = cv.imread('Resources/Pictures/field.jpg')
videoCapture = cv.VideoCapture(1, cv.CAP_DSHOW)
list1 = [0]
circle_list = [0]
while 1:
    ret, image = videoCapture.read()
    if not ret:
        break
    cv.imshow('Read picture', image)
    if cv.waitKey(1) & 0xFF == ord('q'):
        cv.imwrite('Resources/Pictures/fieldWithBalls_concealed.jpg', image)
        break

    # height, width = image.shape[:2]
    # print("height: " + str(height))
    # print("width: " + str(width))
    # print("total pixels: " + str(height * width))
    # blank = np.zeros((480, 640, 3), dtype='uint8')
# cv.imshow('Original picture', image)
# cv.imshow('blank', blank)

# cv.waitKey('q')
videoCapture.release()
cv.destroyAllWindows()

import cv2 as cv
import numpy as np
videoCapture = cv.VideoCapture(1, cv.CAP_DSHOW)
ret, image = videoCapture.read()
height,width=image.shape[:2]
print("height: "+str(height))
print("widt: "+str(width))
print("total pixels: "+str(height*width))


import cv2 as cv

videoCapture = cv.VideoCapture(0)

while True:
    ret, frame = videoCapture.read()
    if not ret:
        break
    
    cv.imshow("Shapes", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

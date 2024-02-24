import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    frame = cv2.line(frame, (10, 450), (10, 10), (0, 80, 0), 5)
    cv2.imshow('Left Frame',frame)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
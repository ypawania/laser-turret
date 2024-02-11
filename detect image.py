import numpy as np
import cv2

cam=cv2.VideoCapture(0)


hueLow=17
hueHigh=29
satLow=70
satHigh=178
valLow=115
valHigh=211

while True:
    ret,  frame = cam.read()
    frameHSV=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerBound=np.array([hueLow,satLow,valLow])
    upperBound=np.array([hueHigh,satHigh,valHigh])
    myMask=cv2.inRange(frameHSV,lowerBound,upperBound)
    cv2.imshow('My Mask',myMask)

    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
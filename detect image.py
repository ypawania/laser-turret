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
    
    contours, _ = cv2.findContours(myMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_contour = max(contours, key=cv2.contourArea, default=None)
    
    # Get bounding box coordinates
    x, y, w, h = cv2.boundingRect(largest_contour)

    # Draw bounding box around the yellow object
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Calculate the center of the bounding box
    center_x = x + w // 2
    center_y = y + h // 2

    ##print(center_x, center_y)
    
    # Display the coordinates on the frame
    cv2.putText(frame, f"Center: ({center_x}, {center_y})", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Yellow Object Tracking', frame)

    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
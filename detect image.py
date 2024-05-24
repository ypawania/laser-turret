import time
import numpy as np
import cv2
import serial

cam=cv2.VideoCapture(0)
ser = serial.Serial(port='COM8', baudrate=9600)

hueLow=17
hueHigh=29
satLow=70
satHigh=178
valLow=115
valHigh=211
angle = 0
while True:
    ret,  frame = cam.read()
    frameHSV=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerBound=np.array([hueLow,satLow,valLow])
    upperBound=np.array([hueHigh,satHigh,valHigh])
    myMask=cv2.inRange(frameHSV,lowerBound,upperBound)
    cv2.imshow('My Mask',myMask)
    
    laserLower=np.array([0, 0, 245])
    laserUpper=np.array([128, 184, 255])
    laserMask=cv2.inRange(frameHSV, laserLower, laserUpper)
    cv2.imshow('Detect Laser', laserMask)
    
    contours, _ = cv2.findContours(myMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_contour = max(contours, key=cv2.contourArea, default=None)
    
    lasercontours, _ = cv2.findContours(laserMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_laser_contour = min(lasercontours, key=cv2.contourArea, default=None)
    
    # Get bounding box coordinates
    x, y, w, h = cv2.boundingRect(largest_contour)
    laserX, laserY, laserW, laserH = cv2.boundingRect(largest_laser_contour)

    # Draw bounding box around the yellow object
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.rectangle(frame, (laserX, laserY), (laserY + laserW, laserY + laserH), (255, 0, 0), 2)
    
    # Calculate the center of the bounding box
    center_x = x + w // 2
    center_y = y + h // 2

    center_x_laser = laserX + laserW // 2
    center_y_laser = laserY + laserH // 2
    
    ##print(center_x, center_y)
    
    # Display the coordinates on the frame
    cv2.putText(frame, f"Center: ({center_x}, {center_y})", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    if (center_x > center_x_laser):
        ser.write(('%X'+(str(angle)) + '#').encode())
        angle += 2
        time.sleep(0.05)
    if (center_x < center_x_laser):
        ser.write(('%X'+(str(angle)) + '#').encode())
        angle -= 2
        time.sleep(0.05)
        
    if (center_y > center_y_laser):
        ser.write(('%Y'+(str(angle)) + '#').encode())
        angle += 2
        time.sleep(0.05)
    if (center_y < center_y_laser):
        ser.write(('%Y'+(str(angle)) + '#').encode())
        angle -= 2
        time.sleep(0.05)

    # Display the frame
    cv2.imshow('Yellow Object Tracking', frame)

    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
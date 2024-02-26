import cv2
import numpy as np
import serial

left = True
right, up, down = False, False, False

cam = cv2.VideoCapture(0)
ser = serial.Serial(port='COM8', baudrate=9600)

while True:
    ret, frame = cam.read()
    frame = cv2.rectangle(frame, (10,10), (620, 450), (0,80,0), 5)
    cv2.imshow('frame', frame)
    
    new = input("Enter Servo Angle: ")
    if (new != 'done'):
        old = new
        ser.write(('%'+ 'X'+(str(new)) + '#').encode())
    elif (new == 'done'):
        leftAngle = old
        
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
ser.close()
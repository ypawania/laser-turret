import cv2
import numpy as np
import serial

##make dictionary for left, right, up, down with bools and angles
##iterate through, and repeat for directions till they are all true 

leftAngle, rightAngle, upAngle, downAngle = 0, 0, 0, 0
old = 0
angleNumber = 0
## 0 = left; 1 = right; 2 = up; 3 = down;


cam = cv2.VideoCapture(0)
ser = serial.Serial(port='COM8', baudrate=9600)

def config():
    global leftAngle, rightAngle, upAngle, downAngle, angleNumber, old
    new = input("Enter Servo Angle: ")
    if (new != 'done'):
        ret, frame = cam.read()
        frame = cv2.rectangle(frame, (10,10), (620, 450), (0,80,0), 5)
        cv2.imshow('frame', frame)
        old = new
        if (angleNumber == 0 or angleNumber == 1):
            axis = 'X'
        elif (angleNumber == 2 or angleNumber == 3):
            axis = 'Y'
        ser.write(('%'+axis+(str(new)) + '#').encode())
    
    elif (new == 'done'):
        match angleNumber:
            case 0:
                leftAngle = old
                print('left angle = ', leftAngle)
            case 1:
                rightAngle = old
                print('rightangle = ', rightAngle)
            case 2:
                upAngle = old
            case 3:
                downAngle = old
            case _:
                print("this should never happen. bad bad bad- ")
        angleNumber += 1
        

while angleNumber < 4:
    
    config()
        
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
ser.close()
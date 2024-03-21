import cv2
import numpy as np

video = cv2.VideoCapture(0)

while True:
    ret,frame = video.read()
    if ret == False: break
    
    cv2.imshow('Frame',frame)
    if cv2.waitKey(1) & 0xFF == ord ('q'):
        break
video.release()
    
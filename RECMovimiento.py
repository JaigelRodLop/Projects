import cv2
import numpy as np

video = cv2.VideoCapture(0)
i=0

while True:
    ret,frame = video.read()
    if ret == False: break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Frame',frame)
    if i == 20:
        bgGray = gray
    if i > 20:
        dif = cv2.absdiff(gray,bgGray)
        cv2.imshow('dif',dif)
    cv2.imshow('Frame',frame)        
    
    i = i + 1
    if cv2.waitKey(1) & 0xFF == ord ('q'):
        break
video.release()
    
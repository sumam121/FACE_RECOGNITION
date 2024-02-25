import cv2 as cv
import numpy as np
import pandas as pd
img=cv.imread("C:/Users/DELL/Pictures/puppy1.jpg")
cv.imshow("Cat",img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('BROO',gray)
# frame=img.read()
def rescaleFrame(img,scale=0.25):
    width=int(img.shape[1]*scale)
    height=int(img.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(img,dimensions,interpolation= cv.INTER_AREA)
capture =cv.VideoCapture( "C:/Users/DELL/Downloads/video_2.mp4") 
while True:
    isTrue, frame = capture.read()
    frame_resized=rescaleFrame(frame,scale=0.2)
    # if cv.waitKey(20) & 0xFF==ord('d'):
    # This is the preferred way - if `isTrue` is false (the frame could 
    # not be read, or we're at the end of the video), we immediately
    # break from the loop. 
    if isTrue:    
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break
cv.imshow()
cv.waitKey(0)
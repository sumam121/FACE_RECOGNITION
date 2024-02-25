import cv2 as cv
img=cv.imread('C:/Users/DELL/Pictures/lady5.jpg')
cv.imshow("Lady",img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("GRAY PERSON",gray)
haar_cascade=cv.CascadeClassifier('haar_cascade.xml')

faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
print(f'No. of faces found={ len(faces_rect)}')

for(x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y) ,( x+w,y+h),(0,255,0), thickness=2)

cv.imshow('Detected Fcaes ', img)

cv.waitKey(0)
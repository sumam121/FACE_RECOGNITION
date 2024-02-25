# print("HELLO WORLD")
# val = input("Enter your value: ") 
# print(val) 
import cv2 as cv
img=cv.imread("C:/Users/DELL/Pictures/puppy1.jpg")
cv.imshow("image", img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('BROO',gray)

canny=cv.Canny(img,125,175)
cv.imshow('canny',canny)
contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found')
cv.waitKey(0)

 
# It is for removing/deleting created GUI window from screen
# and memory
cv.destroyAllWindows()
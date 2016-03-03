import numpy as np
import cv2

img = cv2.imread('img/tstplot.jpg')
gray = cv2.imread('img/tstplot.jpg',0)

ret,thresh = cv2.threshold(gray,127,255,1)

contours,h = cv2.findContours(thresh,1,2)



for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)

    if len(approx)==4:
        if cv2.contourArea(cnt) > 283060.0 :
            print approx, cv2.contourArea(cnt)
            # cv2.drawContours(img,[cnt],0,(0,0,255),-1)

def onmouse(event,x,y,flags,param):
    if( event == cv2.EVENT_MOUSEMOVE ) :
        return
    print x, y
    print img[y][x]

cv2.imshow('img',img)
cv2.setMouseCallback('img',onmouse)
cv2.waitKey(0)
cv2.destroyAllWindows()

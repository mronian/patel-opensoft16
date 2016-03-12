import numpy as np
import cv2

import sys
fname = sys.argv[1]
img1 = cv2.imread(fname)
gray = cv2.imread(fname, 0)
hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)


ret,thresh = cv2.threshold(gray,110,255,1)


img = cv2.medianBlur(gray,5)
     
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)


thresh = th3
contours,h = cv2.findContours(thresh,1,2)

for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True)
    # cv2.drawContours(img1,[cnt],0,(23,25,50),1)
    # # print len(approx)
    # if len(approx)==5:
    #     print "pentagon"
    #     cv2.drawContours(img,[cnt],0,255,-1)
    # # elif len(approx)==3:
    # #     print "triangle"
    # #     cv2.drawContours(img,[cnt],0,(0,255,0),-1)
    # elif len(approx)==4:
    #     # import ipdb; ipdb.set_trace()
    #     print "square"
    #     if cv2.contourArea(cnt) > 283060.0 :
    #         print approx, cv2.contourArea(cnt)
    #         cv2.drawContours(img,[cnt],0,(0,0,255),2)

    # elif len(approx) == 9:
    #     print "half-circle"
    #     cv2.drawContours(img,[cnt],0,(255,255,0),-1)
    # elif len(approx) > 15:
    #     print "circle"
    #     cv2.drawContours(img,[cnt],0,(0,255,255),-1)


def onmouse(event,x,y,flags,param):
    if( event == cv2.EVENT_MOUSEMOVE ) :
        return
    print x, y
    print (cv2.resize(hsv, (2000,1000))[y][x])# / 256.0) * 360.0

import matplotlib.pyplot as plt
# img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
# plt.imshow(img1)
# plt.show()
cv2.imshow("img", cv2.resize(img1, (2000,1000)))
cv2.setMouseCallback('img',onmouse)
cv2.waitKey(0)
cv2.destroyAllWindows()

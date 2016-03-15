import numpy as np
import cv2
from scipy import stats

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

plots = {}


hdelta = 12
def getKey(clr):
    for k in plots.keys():
        if abs(k - clr) < hdelta:
            return k
    return clr

def dcnt(cnts):

    # global img1
    # img1 = img1.copy()
    img1 = cv2.imread(fname)
    for cnt in cnts:
        cv2.drawContours(img1,[cnt],0,(56,122,123),4)

    cv2.imshow("img", img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True)
    
    cnt = cnt.reshape(cnt.shape[0], 1, cnt.shape[2])
    rect = cv2.boundingRect(cnt)
    
    clrs = []

    hs = []
    for i in range(rect[1], rect[1] + rect[3]): 
        for j in range(rect[0], rect[0] + rect[2]):
            if cv2.pointPolygonTest(cnt, (i,j), False):
                if hsv[i][j][2] < 100:
                    continue
                if hsv[i][j][1] < 100 and hsv[i][j][2] > 250 :
                    continue
                hs.append(hsv[i][j][0])

    if len(hs) <= 0:
        continue

    clrMode = stats.mode(hs)
    clr = int(clrMode[0])
    if clrMode[1] > 1:
        print clrMode

    # cv2.drawContours(img1,[cnt],0,(56,0,int(clrMode[0])),4)

    k = getKey(clr)

    if k not in plots.keys():
        plots[k] = []

    plots[k].append(cnt)

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


import ipdb; ipdb.set_trace()
def onmouse(event,x,y,flags,param):
    if( event == cv2.EVENT_MOUSEMOVE ) :
        return
    print x, y
    print hsv[y][x] # / 256.0) * 360.0
    # print (cv2.resize(hsv, (2000,1000))[y][x])# / 256.0) * 360.0

import matplotlib.pyplot as plt
# img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
# plt.imshow(img1)
# plt.show()
# cv2.imshow("img", cv2.resize(img1, (2000,1000)))
cv2.imshow("img", img1)
cv2.setMouseCallback('img',onmouse)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

import sys
filename = 'chessboard.jpg'
filename= sys.argv[1]

img = cv2.imread(filename)

clr = 0
kersize = 22

mainImg = 0

def reload():

    global mainImg 

    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([clr-1,0,0])
    upper_blue = np.array([clr+1,255,250])
    mask = cv2.inRange(img, lower_blue, upper_blue)

    x = kersize
    kernel = np.ones((x,x), np.uint8)
    erosion = cv2.dilate(mask,kernel,iterations = 1)
    erosion = cv2.erode(erosion,kernel,iterations = 1)

    mainImg = np.array(mainImg, dtype=int) + erosion
    cv2.imshow('dst',erosion)

def nothing(x):
    global kersize
    global mainImg 
    kersize = x

    print mainImg.max()
    outm = np.array((mainImg*255.0)/mainImg.max(), dtype=np.uint8)
    cv2.imshow('dst', outm)

    img = cv2.imread(filename)
    img[outm > 200] = [0,0,252]
    mainImg = 0

    ret,thresh = cv2.threshold(outm,200,255,cv2.THRESH_BINARY_INV)
    contours,h = cv2.findContours(thresh,1,2)
    for cnt in contours:
        cv2.drawContours(img,[cnt],0,(0,0,255),4)

    cv2.imshow('dst',thresh)

    # reload()

cv2.imshow('dst',img)


def f(x):
    global clr
    clr = x
    reload()

cv2.createTrackbar('R','dst',20,255,nothing)
cv2.createTrackbar('clr','dst',0,180,f)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()



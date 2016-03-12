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

    img = cv2.imread(filename)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)

    lines = cv2.HoughLines(edges,1,(np.pi*clr)/180,kersize)
    for rho,theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

    cv2.imshow('dst',img)

def nothing(x):
    global kersize
    kersize = x
    reload()

cv2.imshow('dst',img)


def f(x):
    global clr
    clr = x
    reload()

cv2.createTrackbar('R','dst',20,255,nothing)
cv2.createTrackbar('clr','dst',0,180,f)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()



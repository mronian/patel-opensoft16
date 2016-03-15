'''
R Srihari
Returns all the rectangles in a page as array, each element
in the form (topleft-x, topleft-y, bottomright-x, bottomright-y)
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from image import *

def displayimage(img):
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def retrect(img2,rectangles, i, j):
    for k in range(i, len(img2[0])):
        if(img2[j][k]==0):
            pass
        else:
            break
    for m in range(j, len(img2)):
        if(img2[m][i]==0):
            pass
        else:
            break
    if(k-i>50 and m-j>50):
        rectangles.append([ (i,j), (i,m), (k,m), (k,j) ])
        return 1,i, j, k,m
    else:
        return 0,0,0,0,0

def getallrect(img2,rects, xbegin, ybegin, xend, yend):
    flag=0
    try:
        for i in range(xbegin, xend):
            for j in range(ybegin, yend):
                if (img2[j][i]==0):
                    flag,px, py, k,m=retrect(img2,rects, i, j)
                if(flag==1): break
            if(flag==1):
                getallrect(img2, rects,k+2, ybegin, xend, yend)
                getallrect(img2, rects, px, ybegin, k, py-2)
                getallrect(img2, rects,px, m+2, k, yend)
                break
    except:
        pass
    
def getrectangles(img):
    rectangles=[]
    img=img.gray
    top=[]
    bottom=[]
    ret,img2 = cv2.threshold(img,240,255,cv2.THRESH_BINARY)
    getallrect(img2,rectangles, 2,2, len(img2[0]), len(img2))
    return rectangles


        


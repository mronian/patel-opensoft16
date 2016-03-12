import cv2
import numpy as np
import math

def table_check(img,boxcoordinate):


r = .85
margin = 5

    
lx=boxcoordinate[0][0]+margin 
ly=boxcoordinate[3][1]+margin
hx=boxcoordinate[2][0]-margin
hy=boxcoordinate[2][1]-margin

#import pdb; pdb.set_trace()
x=ly-hy
if(x<30)
    r=.7
''' margin taken to avoid inclusion of side edges inconsidering vertical lines
    if table is very small i.e. less than 30 height than to reduce margin error r has been reduced'''
coodinate=[(lx,ly),(lx,hy),(hx,ly),(hx,hy)]
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150)
lines = cv2.HoughLines(edges,1,0.01,int(r*x))
c=0
for line in lines:

    for rho,theta in line:
        
        if theta==0:
            c=c+1
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
            if(theta==0):
                cv2.line(img,(x1,y1),(x2,y2),(10,30,80),1)
if(c>1):
    return True
else :
    return False
''' c is no. of long verticle lines
   r denotes the ratio between side edge and min length of verticle line to be considered
   img can be displayed in end to see how lines are being formed
   returns true if its a table
""

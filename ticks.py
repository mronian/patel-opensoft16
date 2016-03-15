import cv2
import numpy as np

img = cv2.imread("4.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
k,img = ret,thresh1 = cv2.threshold(img,200,255,cv2.THRESH_BINARY)
coordinate=[(368, 254), (368, 378), (509, 254), (509, 378)]

lx=coordinate[0][0]
hx=coordinate[2][0]
ly=coordinate[0][1]
hy=coordinate[3][1]
r=hy+2
textthreshold=5


threshold=2
flag=1
v=0
count=0
coord=[]
r1=0
r2=0
check=0
while (flag==1):
    v=0
    for c in range (lx,hx):
        
        if img[r,c]==0 :
            v=v+1
    

    if v>textthreshold:
        count = count+1
        if check==0 :
            r1=r
        check=1
    if(v<textthreshold):
        v=0
        r2=r
        check=0
        if count >threshold :
            coord.append([(r1,r2)])
        count =0
        if len(coord)==2 :
            break
    
    
    
    r=r+1
    if r-hy>120:
        flag=0
'''    print "v",v,"count",count,"r",r
    print check '''
print coord
ratio=.6
c=lx-1
flag=1
v=0
ycoord=[]
count=0
check
scaletextarea=0
c1=0
c2=0
prev_gap=0
gap=0
while flag==1:
    for r in range( ly,hy):
        if img[r,c]==0 :
            v=v+1

    if v>textthreshold:
        
        count=count+1
        if check==0:
            if gap<prev_gap*ratio:
                scaletextarea=1
            else :
                scaletextarea=0
        if check==0:
            c1=c
            prev_gap=gap
            gap=0
        check=1
    if v<textthreshold:
        if count>threshold and scaletextarea==0:
            ycoord.append([c,c1])
        if check==1:
                gap=0
        gap=gap+1
        check=0
        count=0
    if c==1:
        flag=0
    print "gap", gap, "prev_gap",prev_gap,"scaletextarea",scaletextarea,"v",v,"count",count,"check",check,"c",c
    c=c-1
    v=0
        
print ycoord   
cv2.imshow("output",img)
cv2.waitKey(0)
cv2.destroyAllWindows(0)    

import cv2
import numpy as np

def legendcoordinate(img,coordinate):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    k,img = ret,thresh1 = cv2.threshold(img,245,255,cv2.THRESH_BINARY)

    lx=coordinate[0][0]
    hx=coordinate[2][0]
    ly=coordinate[0][1]
    hy=coordinate[1][1]



    xpad=2
    ypad=2

    v=0
    flag=0
    c=lx
    pixelthresh=7
    check=0

    count=0
    xcoordinate=[]
    c1=0
    c2=0

    r=ly
    v=0
    r=ly
    r1=0
    r2=0
    count=0
    ycoordinate=[]
    height=7
    while r<hy:

        for c in range(lx,hx):
            if img[r][c]==0:
                v=v+1
        if v>pixelthresh:
            if check==0:
                r1=r
            check=1
            count=count+1
        if v<pixelthresh:
            if check==1 and count>height:
                r2=r
                check=0
                count=0
                ycoordinate.append([r1-ypad,r2+ypad])
        
        v=0
        r=r+1
                
            
    output=[]      
    for i in ycoordinate :
        output.append([[lx,i[0]],[lx,i[1]],[hx+2,i[1]],[hx+2,i[0]]])
    return output


    ''



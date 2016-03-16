import cv2
import numpy as np

def readlegend(img , coordinate):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    k,img = ret,thresh1 = cv2.threshold(img,245,255,cv2.THRESH_BINARY)

    lx=coordinate[0][0]
    hx=coordinate[2][0]
    ly=coordinate[0][1]
    hy=coordinate[1][1]

    

    xpad=4
    ypad=4

    v=0
    flag=0
    c=lx
    pixelthresh=5
    check=0
    sumleft=0
    sumright=0
    count=0
    xcoordinate=[]
    c1=0
    c2=0
    while c<hx:
        for r in range(ly,hy):
            
            if img[r][c]==0:
                v=v+1
                if c< lx + int((hx-lx)/2):
                    sumleft=sumleft+1
                if c> lx + int((hx-lx)/2):
                    sumright=sumright+1
                
        if v>pixelthresh:        
            if check==0:
                c1=c
            check=1
            count=count+1
        if v<pixelthresh:
            if check==1 and count>4:
                count=0
                c2=c
                check=0
                xcoordinate.append([c1-xpad,c2+xpad])
        '''print "c",c,"c1",c1,"c2",c2,"v",v,"check",check'''    
        v=0
        c=c+1
    '''print xcoordinate
    for i in xcoordinate :
        print i[0] , i[1]
        cv2.line(img,(i[0],ly),(i[0],hy),(10,30,80),1)    
        cv2.line(img,(i[1],ly),(i[1],hy),(10,30,80),1)'''
    if sumleft>sumright:
        
        l=xcoordinate[0]
        ri=xcoordinate[1]

    r=ly
    v=0
    r1=0
    r2=0
    count=0
    ycoordinate=[]
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
            if check==1 and count>8:
                r2=r
                check=0
                count=0
                ycoordinate.append([r1-ypad,r2+ypad])
        v=0
        r=r+1
                
            
    '''print ycoordinate        
    for i in ycoordinate :
        print i[0] , i[1]
        cv2.line(img,(lx,i[0]),(hx,i[0]),(10,30,80),1)    
        cv2.line(img,(lx,i[1]),(hx,i[1]),(10,30,80),1)'''

    output=[]
    output0=[]
    output1=[]
    '''for i in ycoordinate:
        output0.append([[l[0],i[0]],[l[0],i[1]],[l[1],i[1]],[l[1],i[0]]])

    for i in ycoordinate:
        output1.append([[ri[0],i[0]],[ri[0],i[1]],[ri[1],i[1]],[ri[1],i[0]]])'''
    output.append(output0)
    output.append(output1)
    '''print output
    cv2.imshow("output",img)'''

    return output
    
                


import cv2
import numpy as np


def corner_detection(img):

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img=gray
    c=0
    r=0
    height=0
    length=0
    xhigh=len(img[0])
    yhigh=len(img)

    threshold=240
    def measure (img,r,c,length,height):
        '''returns height , width,and the coordinates of largest box that could be formed around r,c'''
        lx=c
        ly=r
        
        for c1 in range (lx,xhigh):
            ''' to find the max length of line along x from input point c,r'''
            if img[r,c1]<threshold or img [r,c1+1]<threshold :
                length=length+1            
            else :            
                break
            
        for r1 in range (ly,yhigh):
           ''' to find the maximum length of line along y fron input point c,r '''
           if img[r1,c]<threshold or img [r1+1,c]<threshold:
              height=height+1
              
           else :
              break
        
        return r,max(r,r1),c,max(c1,c),height,length,[r,max(r,r1),c,max(c1,c)],[(lx,ly),(lx,max(r,r1-1)),(max(c1-1,c),ly),(max(c1-1,c),max(r,r1-1))]    
        
    ylow=3
    xlow=3
    ''' to prevent detection at edge'''
    r2=ylow
    c2=xlow
    c=xlow
    r=ylow
    corners=[]
    coordinate=[]
    coordinatef=[]
    while r<yhigh-1:
        while c<xhigh-1:   
            for i in corners :
                ''' to prevent working in any area again'''
                if (r>=i[0] and r<=i[1]) and (c>=i[2] and c<= i[3]) :
                    ''' denotes the area already computed before'''
                    c=i[3]
                    '''shifts the c beyond the area'''
            if img[r,c]<threshold:          
                r1,r2,c1,c2,length,height,corner,coordinate1=measure(img,r,c,0,0)
                ''' passing on point to find max box that can be formed around it'''
                corners.append(corner)
                if (length>50 and height>50) :                
                    coordinate.append(coordinate1)
                c=c2
            c=c+1
        r=r+1
        c=xlow
    j=0
    for i in coordinate :
       ''' to prevent counting same boxes again due to line width problem''' 
       if j==0 :
           ''' to skip comparing of first point'''
           coordinatef.append(coordinate[j])
           j=j+1
           continue    
       else :
           
           if abs(coordinate[j][0][0]-coordinate[j-1][0][0])>2 or abs(coordinate[j][0][1]-coordinate[j-1][0][1])>50 :
               coordinatef.append(coordinate[j])
       j=j+1
    return coordinatef

        
    

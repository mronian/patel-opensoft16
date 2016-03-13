#Srihari
#Function findticks(img, corners) returns a tuple of 2d lists of xticks and yticks

import cv2
def findxticks(thresh,corners):
    xstart=corners[1][0]
    xend=corners[2][0]
    ycord=corners[1][1]
    testy=ycord
    pixelnums=xend-xstart
    while(1):
        flag=0
        testy=testy-1
        numinters=0
        inters=[]
        for testx in range(xstart, xend):
            if(thresh[testy][testx]==0):
                numinters+=1
                inters.append([testx, ycord])
        if(numinters<int(0.4*pixelnums) and numinters>0):
            flag=1
            break
    xticks=[]
    prev=0
    for  inter in inters:
        if(inter[0]!=prev+1):
            xticks.append(inter)
        prev=inter[0]
    return xticks

def findleftyticks(thresh,corners):
    ystart=corners[0][1]
    yend=corners[1][1]
    xcord=corners[1][0]
    testx=xcord
    pixelnums=yend-ystart
    while(1):
        flag=0
        testx=testx+1
        numinters=0
        inters=[]
        for testy in range(ystart, yend):
            if(thresh[testy][testx]==0):
                numinters+=1
                inters.append([xcord, testy])
        if(numinters<int(0.4*pixelnums) and numinters>0):
            flag=1
            break
    yticks=[]
    prev=0
    for  inter in inters:
        if(inter[1]!=prev+1):
            yticks.append(inter)
        prev=inter[1]
    return yticks

def findrightyticks(thresh,corners):
    ystart=corners[3][1]
    yend=corners[2][1]
    xcord=corners[2][0]
    testx=xcord
    pixelnums=yend-ystart
    while(1):
        flag=0
        testx=testx-1
        numinters=0
        inters=[]
        for testy in range(ystart, yend):
            if(thresh[testy][testx]==0):
                numinters+=1
                inters.append([xcord, testy])
        if(numinters<int(0.4*pixelnums) and numinters>0):
            flag=1
            break
    yticks=[]
    prev=0
    for  inter in inters:
        if(inter[1]!=prev+1):
            yticks.append(inter)
        prev=inter[1]
    return yticks

def findticks(img, corners):
    gray = img.gray
    ret,thresh = cv2.threshold(gray,230,255,0)
    xticks=findxticks(thresh,corners)
    rightyticks=findrightyticks(thresh,corners)
    leftyticks=findleftyticks(thresh,corners)
    leftyvals=[i[1] for i in leftyticks]
    rightyvals=[i[1] for i in rightyticks]
    yvals=[]
    for i in leftyvals:
        if i in rightyvals:
            yvals.append(i)
    yticks=[]
    xforyticks=leftyticks[0][0]
    yvals=set(yvals)
    yvals=sorted(yvals)
    for tick in yvals:
        yticks.append([xforyticks,tick])  
    return (xticks,yticks)    



    
            
            
                
                
    
	
	

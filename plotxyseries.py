# Srihari
# getxyseries takes in an image where only the relevant plot is present
# getxyseries returns the 2-d list with elements [xcord, ycord]
# Note : For any xcord, the highest point on a thick plot was chosen as y-cord

import cv2

'''corners=[[145,87],[145,536],[860,536],[860,87]]

def drawline(thresh, point1,point2):
    print point1, point2

def drawpic(thresh, xyseries):
    xstart=corners[0][0]
    xend=corners[2][0]
    ystart=corners[0][1]
    yend=corners[1][1]
    for i in range(xstart, xend):
        for j in range(ystart, yend):
            thresh[j][i]=255
    for point in xyseries:
        thresh[point[1]][point[0]]=0
    cv2.imshow('img',thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
'''   

def getxyseries(img, corners):
    thresh=interpolate(img, corners)
    xstart=corners[0][0]
    xend=corners[2][0]
    ystart=corners[0][1]
    yend=corners[1][1]
    xyseries=[]
    for i in range(xstart, xend):
        for j in range(ystart, yend):
            if(thresh[j][i]==0):
                xyseries.append([i, j])
                break
    return xyseries
                
    
def interpolate(img, corners):
    gray=img.gray
    ret,thresh=cv2.threshold(gray, 230, 255,0)
    xstart=corners[0][0]
    xend=corners[2][0]
    ystart=corners[0][1]
    yend=corners[1][1]
    prevx=-1
    prevy=-1
    for i in range(xstart, xend):
        for j in range(ystart, yend):
            if(thresh[j][i]==0):
                if(prevx==i-1 or prevx==-1):
                    pass
                else:
                    cv2.line(thresh, (prevx, prevy),(i,j),color=0, thickness=1)
                prevx=i
                prevy=j
                break
    return thresh

'''
img=Image('img/tstplot2.jpg')
getxyseries(img,corners)
''' 
    
        
        
        
    
    
    
    
    
    
    
    
	

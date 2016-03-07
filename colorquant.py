import cv2
import numpy as np
import helpers

colours = []

def getColor(clr):

    dists = []

    for c in colours:
        dist= helpers.getDistance3(c, clr)
        dists.append(dist)
    
    if len(dists)>0 and min(dists) < 10:
        c = colours[dists.index(min(dists))]
        return c

    colours.append(clr)
    return clr

def processContour(img, cnt):

    cnt = cnt.reshape(cnt.shape[0], 1, cnt.shape[1])
    rect = cv2.boundingRect(cnt)
    
    clrs = []

    for i in range(rect[1], rect[1] + rect[3]): 
        for j in range(rect[0], rect[0] + rect[2]):
            if cv2.pointPolygonTest(cnt, (i,j), False):
                clrs.append(img[i][j])
    
    clrs = np.array(clrs)
    clr = clrs.mean(0)
    # clr = getColor(clr)
    cv2.drawContours(img,[cnt],0,clr,-1)

def getQuantImage(img, corners):
    
    img1 = img.img
    img = cv2.medianBlur(img.gray,5)
         
    ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
    th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)


    thresh = th3
    subimg = helpers.getSubImage(thresh, corners)
    contours,h = cv2.findContours(subimg,1,2)

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
        if cv2.contourArea(cnt) > 300000:
            continue
        approx = cnt
        approx = approx.reshape(approx.shape[0], approx.shape[2])
        approx = approx + corners[0]
        processContour(img1 , approx)

        # cv2.drawContours(img1,[approx],0,(23,25,50),1)

    return img1

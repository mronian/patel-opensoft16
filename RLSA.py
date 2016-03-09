import numpy as np 
import cv2
import os

def getBinary(filename):
    doc=cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    command="ocropus-nlbin -n "+filename+" -o ./"
    os.system(command)

def getSegments(filename):
    img=cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    thresholdh=10
    thresholdw=15

    height, width=img.shape

    element = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
    VAL=0
    doc=img.copy()
    # doc = cv2.dilate(doc, element, iterations=1)
    # doc = cv2.erode(doc, element, iterations=1)

    #RLSA STARTs here
    
    filenamew="Noise2.png"
    cv2.imwrite(filenamew, doc)
    doc2=doc.copy()
    h=w=0
    while(h<height):
        c=1
        while(w<width):
            if doc.item(h,w)==VAL:
                if (w-c)<=thresholdh:
                    for i in xrange(c,w):
                        doc.itemset((h, i), VAL)
                c=w
            w=w+1
        if (width-c)<=thresholdh:
            for i in xrange(c,width):
                doc.itemset((h, i), VAL)
        h=h+1 
        w=0

    #print "Doc 1 Done for "+ str(thresholdh)

    while(w<width):
        c=1
        while(h<height):
            if doc2.item(h,w)==VAL:
                if (h-c)<=thresholdw:
                    for i in xrange(c,h):
                        doc2.itemset((i,w), VAL)
                c=h
            h=h+1
        if (height-c)<=thresholdw:
            for i in xrange(c,height):
                doc2.itemset((i,w), VAL)
        w=w+1 
        h=0
    #print "Doc 2 Done for "+ str(thresholdh)
    cv2.bitwise_and(doc, doc2, doc)
    
    #RLSA ENDs here
    
    doc3 = cv2.erode(doc, element, iterations=3)
    filenamew="Noised.png"
    cv2.imwrite(filenamew, doc3)
    doc3 = cv2.dilate(doc3, element, iterations=3)

    #Contours Start Here
        
    # filenamew="Noisede.png"
    # cv2.imwrite(filenamew, doc3)
    # im, contours, hierarchy=cv2.findContours(doc3, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # counter=1
    # area=0
    # # cv2.namedWindow('Original', cv2.WINDOW_AUTOSIZE)
    # # cv2.createTrackbar('WP','Original',1000,20000,nothing)
    # # while(1):
    # #     tr=0
    # for idx, cnt in enumerate(contours):
    #     area = cv2.contourArea(cnt)
    #     if area>15000:#cv2.getTrackbarPos('WP', 'Original'):
    #         if hierarchy[0][idx][3]==0:
    #             x,y,w,h=cv2.boundingRect(cnt)
    #             cv2.rectangle(doc3,(x,y),(x+w,y+h),(127),2)
    #             img2=img[y:y+h, x:x+w]
    #             filenamew="./static/segments/"+filename.strip('.tif')+"_" + str(counter)+'.png'
    #             cv2.imwrite(filenamew,  img2)
    #             counter=counter+1
    # #print counter
    # filenamew="segmented.png"
    # cv2.imwrite(filenamew, doc3)
    # return counter

    #Contour Ends Here

if __name__ == "__main__":
    import sys
    # getBinary(sys.argv[1])
    getSegments(sys.argv[1])

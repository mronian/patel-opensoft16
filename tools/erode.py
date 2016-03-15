import cv2
import numpy as np

import sys
filename = 'chessboard.jpg'
filename= sys.argv[1]

img = cv2.imread(filename)

clr = 0
kersize = 22

mainImg = 0

erosion = 0

def reload():

    global mainImg 
    global erosion

    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([clr-1,0,0])
    upper_blue = np.array([clr+1,255,250])
    # lower_blue = np.array([0,0,0])
    # upper_blue = np.array([180,255,250])
    mask = cv2.inRange(img, lower_blue, upper_blue)

    x = kersize
    kernel = np.ones((x,x), np.uint8)
    erosion = cv2.dilate(mask,kernel,iterations = 1)
    kernel = np.ones((x/2,x/2), np.uint8)
    erosion = cv2.erode(erosion,kernel,iterations = 1)

    mainImg = np.array(mainImg, dtype=int) + erosion
    cv2.imshow('dst',erosion)

def nothing(x):
    global kersize
    global mainImg 
    kersize = x

    # print mainImg.max()
    # outm = np.array((mainImg*255.0)/mainImg.max(), dtype=np.uint8)
    # cv2.imshow('dst', outm)

    img = cv2.imread(filename)
    # img[outm > 200] = [0,0,252]
    # mainImg = 0

    contours,h = cv2.findContours(erosion,1,2)
    for i,cnt in enumerate(contours):
        cv2.drawContours(img,[cnt],0,(0,i*10 % 255, (i*223)%255  ),4)
    cv2.imshow('dst',img)

    # reload()

# cv2.imshow('dst',img)


def f(x):
    global clr
    global kersize
    clr = x
    reload()


hdelta = 10
def findMaxContours():

    conts = []

    for c in range(180):
    # for c in [170,50,86,111]:

        lower_blue = np.array([c-hdelta,0,0])
        upper_blue = np.array([c+hdelta,255,250])
        mask = cv2.inRange(img, lower_blue, upper_blue)

        x = kersize
        kernel = np.ones((x,x), np.uint8)
        erosion = cv2.dilate(mask,kernel,iterations = 1)
        kernel = np.ones((x/2,x/2), np.uint8)
        erosion = cv2.erode(erosion,kernel,iterations = 1)

        contours,h = cv2.findContours(erosion,1,2)
        for i,cnt in enumerate(contours):
            x,y,w,h = cv2.boundingRect(cnt)
            if w > 0.6 * img.shape[1]:
                app = True
                for cnt2 in conts:
                    if cv2.pointPolygonTest(cnt2, tuple(cnt2[0][0]) , False):
                        app = False
                if app:
                    conts.append(cnt)

    contsS = sorted(conts, key=lambda x: cv2.boundingRect(x)[2] )

    for i,cnt in enumerate(contsS[-90:] ):
        cv2.drawContours(img,[cnt],0,(0,i*10 % 255, (i*223)%255  ),4)
    cv2.imshow('dst',img)

    return contsS[-100:]

findMaxContours()

cv2.createTrackbar('R','dst',20,255,nothing)
cv2.createTrackbar('clr','dst',0,180,f)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()



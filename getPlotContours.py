from imports import *
from helpers import *

hdelta = 1
kersize = 30

def findMaxContours(img):

    conts = []

    for c in range(180):
    # for c in [170,50,86,111]:

        lower_blue = np.array([c-hdelta,0,100])
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
                # for cnt2 in conts:
                #     if cv2.pointPolygonTest(cnt2, tuple(cnt2[0]) , False):
                #         app = False
                if app:
                    conts.append(cnt)

    contsS = sorted(conts, key=lambda x: cv2.boundingRect(x)[2] )

    # for i,cnt in enumerate(contsS[-90:] ):
    #     cv2.drawContours(img,[cnt],0,(0,i*10 % 255, (i*223)%255  ),4)
    # cv2.imshow('dst',img)

    # import pdb; pdb.set_trace()
    return contsS

def getPlotConts(img, corners):

    subImg = img.copy() #getSubImage(img, corners)
    conts = findMaxContours(subImg)
    out = []
    # for cnt in conts:
    #     cnt = cnt.reshape((cnt.shape[0], cnt.shape[2]))
    #     # cnt += corners[0]
    #     out.append(cnt)

    return conts
    return list(reversed(out))

import math
import pytesseract as tess
from PIL import Image
import matplotlib.pyplot as plt
import cv2

def getDistance(p1, p2):
    
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def getDistance3(p1, p2):
    
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2 )

def getMaskedPlot(image, target_color, all_colors):
	"""

	"""
	pass


def getSubImage(img, corners):

    corner_img = img[corners[0][1]:corners[2][1], :]
    corner_img = corner_img[:,corners[0][0]:corners[2][0]]
    return corner_img

def subRange(corners):
    return slice(corners[0][1],corners[2][1]), slice(corners[0][0],corners[2][0])


cnt = 0

def showimg(img, callback=None):

    # im2 = img#cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    # plt.imshow(im2)
    # plt.show()
    # return
    

    global cnt
    def onmouse(event,x,y,flags,param):
        if( event == cv2.EVENT_MOUSEMOVE ) :
            return
        print x, y
        print (img[y][x])# / 256.0) * 360.0

        if callback != None:
            callback(x,y)


    # cnt += 1
    # cv2.imwrite("intimg/%d.png"%cnt, img)
    # return
    cv2.imshow("input", img)
    cv2.setMouseCallback('input',onmouse)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def getOCRText(img, corners, cfg = "-psm 8"):

    # imag = Image.open("img/tstplot.jpg")
    
    if corners != None:
        corner_img = getSubImage(img, corners)
    else:
        corner_img = img
    # cv2.imshow("input", corner_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    imag = Image.fromarray(corner_img)

    # ToDo: for OCR of ticks, use single word
    return tess.image_to_string(imag, config=cfg)




def plotPoints(img, points, clr = (0,255,0), show=True ):

    global cnt
    img = img.copy()
    for p in points:
        cv2.circle(img, (p[0], p[1]), 5, clr, thickness=-1)

    if show:
        # cnt += 1
        # cv2.imwrite("intimg/%d.jpg"%cnt, img)
        # return
        cv2.imshow("input", img)
        # cv2.waitKey(0)
        raw_input()
        cv2.destroyAllWindows()

    return img

def plotMulti(img, series):

    clrs = [
        (0,255,0),
        (0,0,25),
        (0,122,55),
        (23,122,55),
    ]
    
    for i,s in enumerate(series):

        # if len(s) < 10:
        #     continue
        img = plotPoints(img, s, clrs[i%(len(clrs))], False)

    showimg(img)

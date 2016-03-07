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

def getOCRText(img, corners):

    # imag = Image.open("img/tstplot.jpg")
    
    corner_img = img[corners[0][1]:corners[2][1], :]
    corner_img = corner_img[:,corners[0][0]:corners[2][0]]
    # cv2.imshow("input", corner_img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    imag = Image.fromarray(corner_img)

    cfg = "-psm 6"
    return tess.image_to_string(imag, config=cfg)

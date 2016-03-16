from imports import *
from helpers import *
import corners as c

class IMG():
    pass

def extractLegend(image, corners, plots):
    
    corners2 = np.array(corners)
    clipper = np.array([20,20])
    corners2[0] += clipper
    corners2[2] -= clipper
    img = getSubImage(image.img, corners2)
    for p in plots.values():
        cv2.drawContours(img,[p[1] - clipper ],0,(255,255,255),-1)

    x = 22
    lower_blue = np.array([0,0,0])
    upper_blue = np.array([127,127,127])
    mask = cv2.inRange(img, lower_blue, upper_blue)
    kernel = np.ones((x,x), np.uint8)
    erosion = cv2.dilate(mask,kernel,iterations = 1)
    kernel = np.ones((x/2,x/2), np.uint8)
    erosion = cv2.erode(erosion,kernel,iterations = 1)

    showimg(img)


    import pdb; pdb.set_trace()
    img = image.hsv
    lower_blue = np.array([0,0,0])
    upper_blue = np.array([180,255,250])
    mask = cv2.inRange(img, lower_blue, upper_blue)
    mask = cv2.dilate(mask,kernel,iterations = 1)
    mask = np.array(mask, dtype= int)
    mask /= 255

    def f(xval, y):
        blackdots = np.sum(mask[corners[0][1]:corners[2][1], xval] > 250)
        print xval, "->", blackdots

    checkPattern(mask[corners[0][1]:corners[2][1],620:830].sum(axis=1))

    # showimg(image.img, f)
    import pdb; pdb.set_trace()


kernel = np.ones((1,10), np.uint8)

th1 = 50

def checkPattern(col):

    col2 = np.append(col[1:], 0)
    diff = abs(col - col2)
    print col

    i = 0
    def checkP(i):
        if col[i] < 5:
            p1 = 0
            i+=1
            if col[i] > th1:
                while diff[i] < th1:
                    i += 1
                    p1 += 1
                i+=1
                while diff[i] < th1:
                    i += 1
                i+=1
                p2 = 0
                while diff[i] < th1:
                    i += 1
                    p2 += 1

                print abs(p1-p2)
                if abs(p1-p2) < 3:
                    return True
                    
        return False

    for i in range(col.shape[0]):
        try:
            if checkP(i):
                print i
        except:
            pass

    import pdb; pdb.set_trace()
 
def extractLegend(image, corners, plots):
    
    img = image.hsv
    lower_blue = np.array([0,0,0])
    upper_blue = np.array([180,255,250])
    mask = cv2.inRange(img, lower_blue, upper_blue)
    mask = cv2.dilate(mask,kernel,iterations = 1)
    mask = np.array(mask, dtype= int)
    mask /= 255

    def f(xval, y):
        blackdots = np.sum(mask[corners[0][1]:corners[2][1], xval] > 250)
        print xval, "->", blackdots

    checkPattern(mask[corners[0][1]:corners[2][1],620:830].sum(axis=1))

    # showimg(image.img, f)
    import pdb; pdb.set_trace()


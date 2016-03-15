from imports import *

colours = []
mainK = None

allConts = {}

def tshape(m,n, up=True, left = False):

    out = np.zeros((m,n), np.uint8)
    if up:
        out[0,:] = np.ones(n, np.uint8)
    else:
        out[-1,:] = np.ones(n, np.uint8)

    out[:,n/2] = np.ones(m, np.uint8)

    if left:
        return out.transpose()

    return out

def corshape(m, n, up=True, left = False):

    out = np.zeros((m,n), np.uint8)
    if up:
        out[m/2,n/2:3*n/4] = 1
    else:
        out[m/2,n/4:n/2] = 1


    if left:
        out[m/2:3*m/4,n/2] = 1
    else:
        out[m/4:m/2,n/2] = 1

    return out

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
    global mainK

    cnt = cnt.reshape(cnt.shape[0], 1, cnt.shape[1])
    rect = cv2.boundingRect(cnt)
    
    clrs = []

    for i in range(rect[1], rect[1] + rect[3]): 
        for j in range(rect[0], rect[0] + rect[2]):
            if cv2.pointPolygonTest(cnt, (i,j), False):
                clrs.append(img[i][j])
    
    clrs = np.array(clrs)
    clr = clrs.mean(0)

    from scipy import stats
    clrMode = stats.mode(clrs[:,0])

    # print clrMode

    clr = np.array([[(clrMode[0][0], 25,25)]], dtype=np.uint8)

    # clr = getColor(clr)

    # clr = cv2.cvtColor(clr, cv2.COLOR_BGR2HSV)

    return clr[0][0].tolist()


def getQuantImage(image, corners):
    
    img1 = image.img
    img = cv2.medianBlur(image.gray,5)
         
    ret,th1 = cv2.threshold(img,185,255,cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
    th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)


    thresh = th3
    subimg = helpers.getSubImage(thresh, corners)
    contours,h = cv2.findContours(subimg,1,2)

    clrs = {}
    # image.hsv = helpers.getSubImage(image.hsv, corners)
    #
    # for i in range(image.hsv.shape[0]):
    #     for j in range(image.hsv.shape[1]):
    #         h,s,v = image.hsv[i][j]
    #         if v < 5:
    #             continue
    #         if v > 250 and s < 5:
    #             continue
    #         if s < 100:
    #             continue
    #
    #         if h in clrs:
    #             clrs[h] += 1
    #         else:
    #             clrs[h] = 1
    #
    # hist = []
    # for k in clrs:
    #     hist.append((clrs[k],k))
    #
    # hist.sort()
    # import matplotlib.pyplot as plt
    # h = np.array(hist)
    # plt.scatter(h[:,1], h[:,0])
    # plt.show()
    #
    # # import pdb; pdb.set_trace()
    # clrr = hist[-5][1]
    clrr = 150
    lower_blue = np.array([0,0,0])
    upper_blue = np.array([180,255,250])

    # threshold the hsv image to get only blue colors
    mask = cv2.inRange(image.hsv, lower_blue, upper_blue)

    kernel = np.ones((2,4),np.uint8)
    dilation = cv2.dilate(mask,kernel,iterations = 1)
    kernel = np.ones((4,2),np.uint8)
    dilation = cv2.dilate(dilation,kernel,iterations = 1)
    kernel = np.ones((2,100),np.uint8)
    kernel = np.array([
        [1,1,1,1,1,1,1],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0],
        ], np.uint8)

    sze = 300
    kersize = (sze, sze)
    kernel = corshape(kersize[0], kersize[1], False, True)
    dilation = cv2.erode(mask,kernel,iterations = 1)
    dilation += cv2.erode(mask,corshape(kersize[0],kersize[1], True, True),iterations = 1)
    dilation += cv2.erode(mask,corshape(kersize[0],kersize[1], True, False),iterations = 1)
    dilation += cv2.erode(mask,corshape(kersize[0],kersize[1], False, False),iterations = 1)

    kernel = tshape(6,70, True, True)
    kernel = np.ones((10,10), np.uint8)
    erosion = cv2.dilate(mask,kernel,iterations = 1)
    kernel = np.ones((10,10), np.uint8)
    erosion = cv2.erode(erosion,kernel,iterations = 1)
    helpers.showimg(erosion)
    helpers.showimg(mask)

    return

    # import pdb; pdb.set_trace()

    # img1[:,:] = (255,255,255)
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
        if cv2.contourArea(cnt) > 300000:
            continue
        approx = cnt
        approx = approx.reshape(approx.shape[0], approx.shape[2])
        approx = approx + corners[0]
        clr = processContour(image.hsv , approx)
        cv2.drawContours(img1,[approx],0,clr,4)


    return img1

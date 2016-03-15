from imports import *

def findCorners_1(img):

    gray = img.gray

    ret,thresh = cv2.threshold(gray,200,255,cv2.THRESH_BINARY_INV)

    contours,h = cv2.findContours(thresh,1,2)

    # import helpers
    # helpers.showimg(thresh)


    areas = []

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)

        if len(approx)==4:
            ar = cv2.contourArea(cnt)
            areas.append((ar, approx))

            # if cv2.contourArea(cnt) > 103060.0 :
            #     out = approx

    areas = sorted(areas, key= lambda k: k[0])

    out = areas[-1][1]

    return out.reshape((out.shape[0], out.shape[2]))

def findAllRects(img):

    gray = img.gray

    ret,thresh = cv2.threshold(gray,200,255,cv2.THRESH_BINARY_INV)

    contours,h = cv2.findContours(thresh,1,2)

    # import helpers
    # helpers.showimg(thresh)


    areas = []
    outs = []

    for cnt in contours:
        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)

        if len(approx)==4:
            ar = cv2.contourArea(cnt)
            areas.append((ar, approx))

            x,y,w,h = cv2.boundingRect(cnt)

            corn = approx.reshape((approx.shape[0], approx.shape[2]))
            if w > 0.1 * thresh.shape[1] and h > 0.1 *thresh.shape[0]:
                outs.append(corn)

            # if cv2.contourArea(cnt) > 103060.0 :
            #     out = approx


    return outs

    areas = sorted(areas, key= lambda k: k[0])
    out = areas[-1][1]

    return out.reshape((out.shape[0], out.shape[2]))

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
def findCorners_erosion(img):

    lower_blue = np.array([0,0,0])
    upper_blue = np.array([180,255,250])
    mask = cv2.inRange(img.hsv, lower_blue, upper_blue)

    kersize = (min(mask.shape)/2, min(mask.shape)/2)
    kernel = corshape(kersize[0], kersize[1], False, True)
    dilation = cv2.erode(mask,kernel,iterations = 1)
    dilation += cv2.erode(mask,corshape(kersize[0],kersize[1], True, True),iterations = 1)
    dilation += cv2.erode(mask,corshape(kersize[0],kersize[1], True, False),iterations = 1)
    dilation += cv2.erode(mask,corshape(kersize[0],kersize[1], False, False),iterations = 1)

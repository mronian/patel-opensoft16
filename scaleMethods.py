"""
Author: Rohan Raja
"""
import numpy as np
import cv2
import helpers as hlp

def parseScale(img, corners, xticks, xtexts, is_X = True):

    if not is_X:
        xticks.reverse()
        xtexts.reverse()

    xticks = np.array(xticks)
    corners = np.array(corners)

    origin = corners[1]

    _xticks = xticks - origin

    # ToDo: Choose indices such that at the idx, text is present
    idx2 = len(xticks) / 2

    assert idx2 != 0
    idx1 = 0
    idx2 = 1

    # import pdb; pdb.set_trace()

    gotp1 = True
    while gotp1:

        try:
            p1 = float(hlp.getOCRText(img.img, xtexts[idx1]))
            gotp1 =False
        except:
            idx1 +=1
            idx2 +=1
        if idx2 > len(xtexts):
            gotp1 = False

    gotp1 = True
    while gotp1:

        try:
            p2 = float(hlp.getOCRText(img.img, xtexts[idx2]))
            gotp1 =False
        except:
            idx2 +=1

        if idx2 > len(xtexts):
            gotp1 = False

    if is_X:
        m = float(p2 - p1)/float (_xticks[idx2][0] - _xticks[idx1][0])
        b = p1 - m*(_xticks[idx1][0])
    else:
        m = float(p2 - p1)/float (_xticks[idx2][1] - _xticks[idx1][1])
        b = p1 - m*(_xticks[idx1][1])

    

    grainStep = int(float(xticks[1][0]-xticks[0][0])/10.0)
    
    return m,b, grainStep

def reScale(series, corners, xscale, yscale):

    series = np.array(series)
    corners = np.array(corners)
    origin = corners[1]

    _series = series - origin

    allX = _series[:,0]*xscale[0] + xscale[1]
    allY = _series[:,1]*yscale[0] + yscale[1]

    out = np.column_stack((allX, allY))


    grainStep = xscale[2]

    out = out[::grainStep]
    return out

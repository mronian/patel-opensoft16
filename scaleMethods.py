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
    idx2 = 1 # ToDo: Remove this!

    p1 = float(hlp.getOCRText(img.img, xtexts[0]))
    p2 = float(hlp.getOCRText(img.img, xtexts[idx2]))

    if is_X:
        m = float(p2 - p1)/float (_xticks[idx2][0] - _xticks[0][0])
    else:
        m = float(p2 - p1)/float (_xticks[idx2][1] - _xticks[0][1])

    b = p1
    

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

"""
Author: Rohan Raja
"""

import numpy as np
import cv2
import helpers as hlp

params = {

        "colorDelta": 5,
        "lowerSV": [100,50],
        "higherSV": [255,255],
        "kernel": np.ones((2,2),np.uint8),
        "erodeIterations": 1,

}

def extractPlotLine(image, corners, legend_corners, color):

    lower_blue = np.array([color-params["colorDelta"]] + params["lowerSV"] )
    upper_blue = np.array([color+params["colorDelta"]] + params["higherSV"])

    mask = cv2.inRange(image.hsv, lower_blue, upper_blue)

    outMask = np.zeros(mask.shape, dtype=np.uint8)
    sub = hlp.subRange(corners)
    outMask[sub] = mask[sub]
    mask = outMask # Remove everything outside corner box

    # sub = hlp.subRange(legend_corners)
    # mask[sub] = 0 # Remove Legend Box PlotLine

    kernel = params["kernel"]
    erosion = cv2.erode(mask,kernel,iterations = params["erodeIterations"])

    compliment = 255 - erosion
    return compliment

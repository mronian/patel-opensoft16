"""
Author - Rohan Raja (rohanraja9@gmail.com)
"""

import numpy as np
import helpers
import cv2
from helpers import *
from getbounds import getbounds

epsilon = 30
delta = 4
ystart_padding = 1
yinc = 15
WHITE_CLR = (255,255,255)

def getTicksText(image, corners, xticks, bounds):

    img = image

    xticks = np.array(xticks)
    tick = xticks[1]
    mid_left = (xticks[0]  + xticks[1])/2
    mid_right = (xticks[1]  + xticks[2])/2

    ystart, yend = bounds[0][0]
    ystart -= ystart_padding
    yend += ystart_padding

    out = []

    mid_dist = tick - mid_left
    y_up = np.array([0, ystart])
    y_down = np.array([0, yend])

    for tick in xticks:
      rect = []
      x_left = tick - mid_dist
      x_right = tick + mid_dist
      x_left[1] = 0
      x_right[1] = 0

      rect.append(x_left + y_up)
      rect.append(x_left + y_down)
      rect.append(x_right + y_down)
      rect.append(x_right + y_up)

      out.append(rect)

    return out

def getYTicksText(image, corners, yticks, bounds):

    img = image

    xticks = np.array(yticks)
    tick = xticks[1]
    mid_left = (xticks[0]  + xticks[1])/2
    mid_right = (xticks[1]  + xticks[2])/2

    yend, ystart = bounds[1][0]
    out = []

    mid_dist = tick - mid_left
    y_up = np.array([ystart, 0])
    y_down = np.array([yend, 0])

    for tick in xticks:
      rect = []
      x_left = tick - mid_dist
      x_right = tick + mid_dist
      x_left[0] = 0
      x_right[0] = 0

      rect.append(x_left + y_down)
      rect.append(x_right + y_down)
      rect.append(x_right + y_up)
      rect.append(x_left + y_up)

      out.append(rect)



    return out


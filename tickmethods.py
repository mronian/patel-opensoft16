"""
Author - Rohan Raja (rohanraja9@gmail.com)
"""

import numpy as np
import helpers

epsilon = 30
delta = 4
ystart_padding = 1
yinc = 1
WHITE_CLR = (255,255,255)

def getTicksText(image, corners, xticks):
    """
    image - Image class instance from image.py
    corners - Array of 4 points of corners - 
              Order of points in array is :

              Index    Position
              0        Top left
              1        Bottom left
              2        Bottom right
              3        Top right


    xticks - array of tick coordinates

    output: array of rectangle surrounding tick text
    """

    img = image.img

    xticks = np.array(xticks)
    tick = xticks[1]
    mid_left = (xticks[0]  + xticks[1])/2
    mid_right = (xticks[1]  + xticks[2])/2

    ystart = tick[1]

    while helpers.getDistance3(img[ystart][tick[0]], WHITE_CLR  ) > epsilon:
      ystart += 1
    
    ystart += ystart_padding

    yend = ystart

    seenBlack = 0
    seenPureWhite = 0

    while seenBlack == 0 or seenPureWhite == 0 :

      colorAvg = img[yend][mid_left[0]:mid_right[0]].mean(0)
      dist = helpers.getDistance3(colorAvg, WHITE_CLR)

      if dist > delta:
        if seenBlack == 0:
          ystart = yend - yinc - ystart_padding
          seenBlack = 1

      elif seenBlack == 1:
        seenPureWhite = 1
      yend += yinc

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


    # import pdb; pdb.set_trace()

    return out

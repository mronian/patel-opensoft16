"""
Author - Rohan Raja (rohanraja9@gmail.com)
"""

import numpy as np
import helpers
import cv2

epsilon = 30
delta = 4
ystart_padding = 1
yinc = 15
WHITE_CLR = (255,255,255)

def findClosestCont(conts, point):

  minDist = 1000
  minCnt = None

  for cnt in conts:
    for p in cnt:
        # import pdb; pdb.set_trace()
        dist = helpers.getDistance(point, p)
        if dist < minDist:
          minDist = dist
          minCnt = cnt

  return minCnt

def find_ymax(conts):
    
  ys = []

  for cnt in conts:
    ys.append(cnt[:,1].max())

  y_max = np.min(ys)
    
  ys = []
  for cnt in conts:
    ys.append(cnt[:,1].min())

  y_min = np.min(ys)

  return y_min, y_max

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

    img = image

    xticks = np.array(xticks)
    tick = xticks[1]
    mid_left = (xticks[0]  + xticks[1])/2
    mid_right = (xticks[1]  + xticks[2])/2

    ystart = tick[1]
    subcorners = [
        corners[1],
        (corners[1][0], img.shape[0]),
        (corners[2][0], img.shape[0]),
        corners[2],
    ]
    subimg = helpers.getSubImage(img, subcorners)

    ret,thresh = cv2.threshold(subimg,127,255,1)
    contours,h = cv2.findContours(thresh,1,2)
    conts = []
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt,0.1*cv2.arcLength(cnt,True),True)
        approx = approx.reshape(approx.shape[0], approx.shape[2])
        approx = approx + corners[1]
        conts.append(approx)

        # cv2.drawContours(img,[approx],0,(0,255,255),2)


    cnt2 = findClosestCont(conts, xticks[4])
    # helpers.plotPoints(img, cnt2)
    # cv2.drawContours(img,[cnt2],0,(0,255,255),4)

    # helpers.showimg(img)

    # ystart = cnt2[:,1].min() - ystart_padding
    # yend = cnt2[:,1].max() + ystart_padding

    ystart, yend = find_ymax(conts)
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


    # import pdb; pdb.set_trace()

    return out

def getTicksText2(image, corners, xticks):
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

    img = image

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

def getYTicksText(image, corners, yticks):

    img = image

    xticks = np.array(yticks)
    tick = xticks[1]
    mid_left = (xticks[0]  + xticks[1])/2
    mid_right = (xticks[1]  + xticks[2])/2

    ystart = tick[0]

    while helpers.getDistance3(img[tick[1]][ystart] , WHITE_CLR  ) > epsilon:
      ystart -= 1
    
    ystart += ystart_padding

    yend = ystart

    seenBlack = 0
    seenPureWhite = 0

    while seenBlack == 0 or seenPureWhite == 0 :

      colorAvg = img[mid_left[1]:mid_right[1] , yend].mean(0)
      dist = helpers.getDistance3(colorAvg, WHITE_CLR)

      if dist > delta:
        if seenBlack == 0:
          # ystart = yend + yinc + ystart_padding
          seenBlack = 1
      elif seenBlack == 1:
        seenPureWhite = 1
      yend -= yinc

    yend -= ystart_padding

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

  # # image_transp = image.transpose((1,0,2))
  # yticks_inverted = []
  #
  # for ytk in yticks:
  #   yticks_inverted.append(list(reversed(ytk)))
  #
  # return getTicksText(image_transp, corners,  yticks_inverted)



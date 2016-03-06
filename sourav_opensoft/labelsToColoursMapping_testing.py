''' 
    Sourav Mohanty
    souravmohanty07@gmail.com
'''

import numpy as np
import cv2
import matplotlib.pyplot as plt

def isColorPresent(image,iStart,iEnd,jStart,jEnd,colorSet):
    """ 
        input--
            isColorPresent(image,iStart,iEnd,jStart,jEnd,colorSet)
        output--
            Returns (isPresent(boolValue) , tupleOfColor)
    """
    lenColor = len(colorSet)
    i= iStart
    while(i<=iEnd):
        j=jStart
        while(j<=jEnd):
            valRGB = tuple(image[i][j])
            for color in range(lenColor):
                if(colorSet[color]==valRGB):
                    return (True,valRGB)
            j+=1
        i+=1
    return (False,(-1,-1,-1))
    

def labelsToColoursMapping(image,legendBoundaryCorners,stringToCornersDict,colorSet):
    
    """
    Returns the Dictionary of Strings and color Tuples
	Input:
		image : RGB values (0 to 255 each)
		legendBoundaryCorners : 2D array of coordinates ( assumed order to be TLeft,TRight,BRight.....) 
		stringToCornersDict : string mapped to 2d array of corners
		colorSet : set of tuples of RGB values (0 to 255 each)
	Output:
		stringToColourDict : each string mapped to corresponding colours
    """
    ### i -> vertical
    ### j -> horizontal
    [iMin,jMin] = legendBoundaryCorners[0]    
    [iMax,jMax] = legendBoundaryCorners[2]
    stringToColorDict = {}
    for element in stringToCornersDict:
        [iStart,jStart] = stringToCornersDict[element][0]
        [iEnd,jEnd] = stringToCornersDict[element][2]
        ### check Left
        jMinLR,jMaxLR = jMin,jStart-1
        (isPresent,color) = isColorPresent(image,iStart,iEnd,jMinLR,jMaxLR,colorSet)
        if(isPresent):
            stringToColorDict[element] = color
            continue
        ### check Right
        jMinLR,jMaxLR = jEnd+1,jMax
        (isPresent,color) = isColorPresent(image,iStart,iEnd,jMinLR,jMaxLR,colorSet)
        stringToColorDict[element] = color
        
    return stringToColorDict
    
#######################################################################################################
sample_image = cv2.imread("/home/sourav/Desktop/Open_soft/tstplot.jpg")

## hardcoded
stringToCornersDict1 = {}
stringToCornersDict1['APPS'] = [[325,650],[325,736],[356,736],[356,650]]
stringToCornersDict1['BS500'] = [[359,640],[359,736],[382,736],[382,640]]
stringToCornersDict1['BS1000'] = [[385,625],[385,736],[410,736],[410,625]]
stringToCornersDict1['BS2000'] = [[413,627],[413,736],[435,736],[435,627]]
stringToCornersDict1['AWA'] = [[440,651],[440,736],[462,736],[462,651]]
stringToCornersDict1['ANA'] = [[467,656],[467,736],[489,736],[489,656]]
stringToCornersDict1['DFBB'] = [[492,651],[492,736],[516,736],[516,651]]

legendBoundaryCorners1 = [[314,623],[314,839],[520,839],[520,623]]

colorSet1 = [(29,9,246),(70,196,97),(188,84,55),(156,81,187),(215,200,127),(15,240,249),(1,1,1)]

stringToColorDict1 = labelsToColoursMapping(sample_image,legendBoundaryCorners1,stringToCornersDict1,colorSet1)

### hardcoded


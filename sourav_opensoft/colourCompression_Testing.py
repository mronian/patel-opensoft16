import numpy as np
import cv2
import matplotlib.pyplot as plt
import time


def colorIndexUsingDist(pixelValue,colorSet):
    """
        returns the index of color using "Euclidean distance" similarity
        Input - 
            pixel value in tuple
            2D array of colors
        Output - 
            index of the color it belongs.
    """
    minDistCheck = []
    index = 0
    for color in colorSet:
        minDistCheck.append([sum(np.square(pixelValue-color)),index])
        index += 1
    minDistCheck = sorted(minDistCheck)
    return minDistCheck[0][1]

####################################

def colorIndexUsingRange(pixelValue,colorSet):
    
    """
        returns the index of color using "Range" similarity
        Input - 
            pixel value in tuple
            2D array of colors
        Output - 
            index of the color it belongs.
    """
    
    index = 0
    rgbRange = np.ones(3,dtype = int)*20
    for color in colorSet:
        lower = color - rgbRange
        upper = color + rgbRange
        if((lower[0]<=pixelValue[0]<=upper[0]) and (lower[1]<=pixelValue[1]<=upper[1]) and (lower[2]<=pixelValue[2]<=upper[2]) ):
            return index
        index+=1
    return 0
        
#######################################

def compressImageColours(image,colorSet):
    
    """
        Returns compressed Image
    """
    
    image = np.array(image)
    colorSet = np.array(colorSet)
    w, h, d = tuple(image.shape)
    for i in range(w):
        for j in range(h):
            image[i][j] = colorSet[colorIndexUsingDist(image[i][j],colorSet)]
            
    return image

#########################################################################

colorRange = [([117, 49, 136], [157, 89, 176]), ([141, 79, 163], [181, 119, 203]), ([168, 180, 92], [208, 220, 132]), ([22, 15, 42], [62, 55, 82]), ([193, 214, 199], [233, 254, 239]), ([90, 159, 114], [130, 199, 154])]
colorCluster = [[255,255,255]]

for (lower,upper) in colorRange:
    RGBMean = (np.array(lower) + np.array(upper))/2
    colorCluster.append(RGBMean)
colorCluster = np.array(colorCluster)

sample_image = cv2.imread("/home/sourav/Desktop/Open_soft/tstplot.jpg")

#########################################################################

t0 = time.time()
img = compressImageColours(sample_image,colorCluster)
print("done in %i secs." % int(time.time() - t0))
img = np.array(img, dtype=np.float64) / 255
plt.imshow(img)
plt.show()


    
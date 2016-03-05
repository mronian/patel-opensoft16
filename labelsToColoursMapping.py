''' 
    Sourav Mohanty
    souravmohanty07@gmail.com
    
'''
def isColorPresent(image,iStart,iEnd,jStart,jEnd,colorSet):
    """ 
        Input-->
            isColorPresent(image,iStart,iEnd,jStart,jEnd,colorSet)
        Output-->
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
		legendBoundaryCorners : 2D array of coordinates ( assumed order to be TopLeft,TopRight,ButtomRight.....) 
		stringToCornersDict : string mapped to 2D array of corner points
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
    

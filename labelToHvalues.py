import cv2

def isColorPresent(image,iStart,iEnd,jStart,jEnd,colorSet):
    """ 
        input--
            isColorPresent(image,iStart,iEnd,jStart,jEnd,colorSet)
        output--
            Returns (isPresent(boolValue) , hColor)
    """
    tup = {}
    j = jStart
    while(j<=jEnd):
        i= iStart
        while(i<=iEnd):
            valH = image[i][j][0]
            if(tup.has_key(valH)):
                tup[valH]+=1
            else:
                tup[valH]=1
            i+=1
        j+=1
    tup[0]=0
    arTup = []
    for key in tup.keys():
        arTup.append(tuple([tup[key],key]))
    arTup = sorted(arTup,reverse =True)
    (count,colValue) = arTup[0]
    for color in colorSet:
        if((color-5)<=colValue<=(color+5)):
            return color,count
    return -1,-1

def labelsToColoursMapping(image,stringToCornersDict,colors):
    
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
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h=hsv[:,:,1]  ## only taken 's' component
    h1 = hsv[:,:,2]
    mask1 = cv2.inRange(h1,0,100)
    hsv = hsv - cv2.bitwise_and(hsv,hsv,mask = mask1)
    # define range of saturation vaue to filter out in HSV
    lower = 50 # dynammic variable
    upper = 255
    mask = cv2.inRange(h, lower, upper)
    # remove all the noise as they have low saturation value
    image = cv2.bitwise_and(hsv,hsv, mask = mask)
    
    iMin = 10000
    jMin = 10000
    iMax = -1
    jMax = -1
    for values in stringToCornersDict.values():
        iMin = min(values[0][1],iMin) ## y axis
        jMin = min(values[0][0],jMin) ## x axis
        iMax = max(values[2][1],iMax) ## y axis
        jMax = max(values[2][0],jMax) ## x axis
      
    dis = (jMax-jMin)/2
    jMin-=dis
    jMax+=dis   
    stringToColorDict = {}
    for element in stringToCornersDict:
        [jStart,iStart] = stringToCornersDict[element][0]
        [jEnd,iEnd] = stringToCornersDict[element][2]
     
        ### check Left
        jMinLR,jMaxLR = jMin,jStart-1
        (color,count) = isColorPresent(image,iStart,iEnd,jMinLR,jMaxLR,colors)
        ### check Right
        jMinLR,jMaxLR = jEnd+1,jMax
        (color2,count2) = isColorPresent(image,iStart,iEnd,jMinLR,jMaxLR,colors)
        if(count2<count):
            stringToColorDict[element] = color
        else:
            stringToColorDict[element] = color2
    
    hValueToString = {}
    for key in stringToColorDict.keys():
        if(stringToColorDict[key]!=-1):
            hValueToString[stringToColorDict[key]]=key
        
    return hValueToString
    
#######################################################################################################

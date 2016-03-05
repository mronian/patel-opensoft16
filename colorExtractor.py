
def getColors(image,legend_corners):
	"""
	Returns the set of color tuples in the Image

	Input:
		Image
		Legend_Corners : List of tuples of coordinates of x-y
		Text_Box_Corners : List of tuples of tuples of coordinates x-y in 
	Output:
		List of tuples of all the colors (except black and white) in Image
	"""
        colors = [([0,0,0],[20,20,20]),([235,235,235],[255,255,255])]
        # Legend_Corner coordinates
        lr = legend_corners[0,1] 
        ur = legend_corners[1,1]
        lc = legend_corners[0,0]
        uc = legent_corners[2,0]
        # Loop
        for r in range(lr,ur):
            for c in range(lc,uc):
                    p = 1
                    for (lower,upper) in colors:
                        if(~(((output[r,c,0]<lower[0])|(output[r,c,0]>upper[0]))&((output[r,c,1]<lower[1])|(output[r,c,1]>upper[1]))&((output[r,c,2]<lower[2])|(output[r,c,2]>upper[2])))):
                                    p = 0
                                    break
                    if(p):
                            a = ([max(output[r,c,0]-20,0),max(output[r,c,1]-20,0),max(output[r,c,2]-20,0)],[min(output[r,c,0]+20,255),min(output[r,c,1]+20,255),min(output[r,c,2]+20,255)])
                            colors.append(a)
        colors.pop(0) # Removes Black Color
        colors.pop(0) # Removes White Color
        return boundaries

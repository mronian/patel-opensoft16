
def getColors(image,corners,legend_corners):
	"""
	Returns the set of color tuples in the Image

	Input:
		Image
		Corners : List of tuples of coordinates x-y
		Legend_Corners : List of tuples of coordinates of x-y
	Output:
		List of tuples of all the colors (except black and white) in Image
	"""
        boundaries = [([0,0,0],[20,20,20]),([235,235,235],[255,255,255])]
        # Corner coordinates
        lr = corners[0,1] 
        ur = corners[1,1]
        lc = corners[0,0]
        uc = corners[2,0]
        # Vertical Box
        for r in range(lr,ur):
            for c in range(lc,uc):
                    p = 1
                    for (lower,upper) in boundaries:
                        if(~(((output[r,c,0]<lower[0])|(output[r,c,0]>upper[0]))&((output[r,c,1]<lower[1])|(output[r,c,1]>upper[1]))&((output[r,c,2]<lower[2])|(output[r,c,2]>upper[2])))):
                                    p = 0
                                    break
                    if(p):
                            colors.append(output[r,c])
                            a = ([max(output[r,c,0]-20,0),max(output[r,c,1]-20,0),max(output[r,c,2]-20,0)],[min(output[r,c,0]+20,255),min(output[r,c,1]+20,255),min(output[r,c,2]+20,255)])
                            boundaries.append(a)
        '''# Horizontal Box
        for r in range(lr,ur):
                for c in range((uc+lc)/2 - 25,(uc+lc)/2 +25):
                        p = 1
                        for (lower,upper) in boundaries:
                                if(~(((output[r,c,0]<lower[0])|(output[r,c,0]>upper[0]))&((output[r,c,1]<lower[1])|(output[r,c,1]>upper[1]))&((output[r,c,2]<lower[2])|(output[r,c,2]>upper[2])))):
                                        p = 0
                                        break
                                if(p):
                                        a = ([max(output[r,c,0]-20,0),max(output[r,c,1]-20,0),max(output[r,c,2]-20,0)],[min(output[r,c,0]+20,255),min(output[r,c,1]+20,255),min(output[r,c,2]+20,255)])
                                        boundaries.append(a)'''
        boundaries.pop(0)
        boundaries.pop(0)
        return boundaries

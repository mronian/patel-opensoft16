''' 
    Sourav Mohanty
    souravmohanty07@gmail.com
'''

import numpy as np

def colourMasking(image,boundaryCorners,targetColour):
    """
    Returns the Masked Image
	Input:
		Image : RGB values (0 to 255 each)
		BoundaryCorners : 2D array of coordinates ( assumed order to be TLeft,TRight,BRight.....) 
		colourToBeMasked : tuple of RGB values (0 to 255 each)
	Output:
		Masked Image
    """
    [istart,jstart]=  boundaryCorners[0]
    [iend,jend] =  boundaryCorners[2]
    # Load Image and transform to a 2D numpy array.
    image_array = np.array(image)
    targetColourArray = np.array(targetColour)
    w, h, d = tuple(image.shape)
    assert d == 3
    #image_array = np.reshape(image, (w * h, d))
    masked_image = np.ones((w, h, d))
    masked_image = masked_image*255
    i=istart
    j=jstart
    while(i<=iend):
        j=jstart
        while(j<=jend):
            if(tuple(image_array[i][j])==targetColour):
                masked_image[i][j] = targetColourArray
            j+=1
        i+=1
                 
    masked_image = np.array(masked_image, dtype = np.uint8)
    return masked_image
    

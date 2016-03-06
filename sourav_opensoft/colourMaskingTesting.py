import numpy as np
import cv2
import matplotlib.pyplot as plt

def colourMasking(image,boundaryCorners,targetColour):
    """
    Returns the Masked Image
	Input:
		Image : RGB values (0 to 255 each)
		BoundaryCorners : List of tuples of coordinates ( assumed order to be TLeft,TRight,BRight.....) 
		colourToBeMasked : tuple of RGB values (0 to 255 each)
	Output:
		Masked Image
    """
    [istart,jstart]=  corners[0]
    [iend,jend] =  corners[2]
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
# [(1, 1, 1), (53, 150, 53), (86, 86, 255), (205, 202, 198), (255, 27, 28), (255, 255, 255)]

sample_image = cv2.imread("/home/sourav/Desktop/Open_soft/tstplot.jpg")
#dum = np.array(sample_image,dtype=np.float64) / 255
#plt.imshow(sample_image)
#plt.show()
corners = [[0,0],[0,948],[668,948],[668,0]]
col = tuple([1,1,1])
#sample_image_out = np.array(colourMasking(sample_image,col),dtype=np.float64) / 255
sample_image_out = colourMasking(sample_image,corners,col)
plt.figure()
plt.imshow(sample_image_out)
plt.show()
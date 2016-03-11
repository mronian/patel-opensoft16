import cv2
import numpy as np
import matplotlib.pyplot as plt

sample_image = cv2.imread("/home/sourav/Desktop/Open_soft/tstplot11.png")



def local_maxima(xval, yval):
    xval = np.asarray(xval)
    yval = np.asarray(yval)

    sort_idx = np.argsort(xval)
    yval = yval[sort_idx]
    gradient = np.diff(yval)
    maxima = np.diff((gradient > 0).view(np.int8))
    return np.concatenate((([0],) if gradient[0] < 0 else ()) +
                          (np.where(maxima == -1)[0] + 1,) +
                          (([len(yval)-1],) if gradient[-1] > 0 else ()))
                          
                          
# Convert BGR to HSV
hsv = cv2.cvtColor(sample_image, cv2.COLOR_BGR2HSV)
h=hsv[:,:,1]  ## only taken 's' component


# define range of saturation vaue to filter out in HSV
lower_blue = 50  # dynammic variable
upper_blue = 255

mask = cv2.inRange(h, lower_blue, upper_blue)

# remove all the noise as they have low saturation value
res = cv2.bitwise_and(hsv,hsv, mask = mask)
plt.figure(1)
plt.imshow(res)

w,h,d = res.shape

hvalue_freq = [0]*180

for i in range(w):
    for j in range(h):
        if(mask[i][j] != 0):
            hvalue_freq[res[i][j][0]]+=1
## If want to check by joining first and last part          
#hvalue_freq.extend(hvalue_freq)
#plt.plot(range(360),hvalue_freq,linewidth = 1.0)

# Plot for only 180 components
plt.figure(2)
plt.plot(range(180),hvalue_freq,linewidth = 1.0)

locMax = local_maxima(range(180),hvalue_freq)
maxValue = []
locMax_thresh = []

freqCountThresh = 70 # dynammic variable
""" proximityThresh = yeh kaise lun samajh nahin aa raha hai """

for i in locMax:
    if(hvalue_freq[i]>freqCountThresh):
        maxValue.append(hvalue_freq[i])
        locMax_thresh.append(i)
    
plt.plot(locMax_thresh,maxValue,'ro')
plt.show()
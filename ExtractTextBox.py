import cv2
import numpy as np

def get_legend_textbox(image,plot_coordinates, plots):
    '''
        Input
         --> Image (with all the plot borders removed)

         Output
         --> legend_text_coordinates (contains coordinates of the legend text)
    '''

    BLACK_MIN = np.array([0, 0, 0],np.uint8)
    BLACK_MAX = np.array([180, 255,62],np.uint8)
    hsv_img = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    frame_threshed = cv2.inRange(hsv_img, BLACK_MIN, BLACK_MAX)
    x = 0
    p = 1
    while(p):
        frame_threshed = cv2.dilate(frame_threshed,np.ones((3,3)),iterations=x)
        contours,hierarchy = cv2.findContours(frame_threshed, 1, 2)
        if(len(contours)>1):
            x = x+1
        else:
            p = 0
            for cnt in contours:
                x,y,w,h = cv2.boundingRect(cnt)
                legend_text_coordinates = [(x,y),(x,y+h),(x+w,y),(x+w,y+h)]
                return legend_text_coordinates 

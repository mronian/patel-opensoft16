import cv2
import numpy as np

def legend_text_box_coordinates(image,corners,thresh):
    '''
        Input
            -> Image
            -> Corner Coordinates (plot)
            -> thresh (threshold frequency of a color occuring in a vertical strip)
        Output
            -> legend_text_box_corners(a list of tupples containing coordinates of the legend text box
    '''


    '''
        Code to remove rectangles from the image
            -> First rectangle bounding the plot
            -> Second rectangle bounding the legend if present

        Store the modified image in image variable itself

     ===>if second rectangle (legend bounding) is present then set the flag to 1
            and store the coordinates in legend_corners

    '''
    if(flag):
        lr = legend_corners[0,1]
        ur = legend_corners[1,1]
        lc = legend_corners[0,0]
        uc = legend_corners[2,0]
        for c in xrange(uc,lc,-10):
            scu = c
            scl = c-20
            p = 0
            count = [0]
            colors = [([230,230,230],[255,255,255])]
            for r in xrange(lr,ur,3):
                temp = [([230,230,230],[255,255,255])]
                for x in xrange(suc,slc,-2):
                    p = 1
                    for(lower,upper) in temp:
                        if(~(((image[r,c,0]<lower[0])|(image[r,c,0]>upper[0]))&((image[r,c,1]<lower[1])|(image[r,c,1]>upper[1]))&((image[r,c,2]<lower[2])|(image[r,c,2]>upper[2])))):
                            p = 0
                            break
                    if(p):
                        temp.append()
                        break
                    
                for (lower,upper) in temp:
                    x = [(lower[0]+upper[0])/2,(lower[1]+upper[1])/2,(lower[1]+upper[1])/2]
                    t = 0
                    p = 1 # Flag
                    for (l,u) in colors:
                        if(~(((x[0]<l[0])|(x[0]>u[0]))&((x[1]<l[1])|(x[1]>u[1]))&((x[2]<l[2])|(x[2]>u[2])))):
                            count[t] += 1
                            p = 0
                            break
                        t = t + 1
                    if(p):
                        colors.append()
                        count.append(1)
                
            colors.pop(0) # Removing White Color
            count.pop(0) # Removing count for White Color
            if (max(count)>thresh):
                if(abs(c-uc)>abs(c-lc)):
                    legend_text_box_corners = [(lc,lr),(lc,ur),(c,lr),(c,ur)]
                break
            else:
                continue

    else:
        lr = corners[0,1]
        ur = corners[1,1]
        lc = corners[0,0]
        uc = corners[2,0]
        
        
                    
    return legend_text_box_corners
        
    
        
        
        
                        
                        
                        
                
                
                
                        
                       
                    
                
    

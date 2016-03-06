
def getColors(image,legend_corners,legend_text_corners,off):
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
        leg_lr = legend_corners[0,1] 
        leg_ur = legend_corners[1,1]
        leg_lc = legend_corners[0,0]
        leg_uc = legent_corners[2,0]
        
        # Legend text Corner coordinates
        txt_lr = legend_text_corners[0,1]
        txt_ur = legend_text_corners[1,1]
        txt_lc = legend_text_corners[0,0]
        txt_uc = legend_text_corners[2,0]

        # Calculating the Color region coordinates
        if(abs(txt_lc - leg_lc) > abs(txt_lc - leg_uc)):
                lc = leg_lc
                uc = txt_lc
                lr = leg_lr
                ur = leg_ur
        elif(abs(txt_lc - leg_lc) == abs(txt_lc - leg_uc)):
                if(abs(txt_uc - leg_lc) > abs(txt_uc - leg_uc)):
                        lc = leg_lc
                        uc = txt_lc
                        lr = leg_lr
                        ur = leg_ur
                else:
                        lc = txt_uc
                        uc = leg_uc
                        lr = leg_lr
                        ur = leg_ur
        else:
                lc = txt_uc
                uc = leg_uc
                lr = leg_lr
                ur = leg_ur  
        # Loop
        for r in range(lr,ur):
            for c in range(lc,uc):
                    p = 1
                    for (lower,upper) in colors:
                        if(~(((image[r,c,0]<lower[0])|(image[r,c,0]>upper[0]))&((image[r,c,1]<lower[1])|(image[r,c,1]>upper[1]))&((image[r,c,2]<lower[2])|(image[r,c,2]>upper[2])))):
                                    p = 0
                                    break
                    if(p):
                            a = ([max(image[r,c,0]-off,0),max(image[r,c,1]-off,0),max(image[r,c,2]-off,0)],[min(image[r,c,0]+off,255),min(image[r,c,1]+off,255),min(image[r,c,2]+off,255)])
                            colors.append(a)
        colors.pop(0) # removes Black color
        colors.pop(0) # removes white color
        return boundaries

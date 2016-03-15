"""
Rohit
"""
import cv2

pad = 3
def getbounds(img,coordinate):

    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    k,img = ret,thresh1 = cv2.threshold(img,200,255,cv2.THRESH_BINARY)

    lx=coordinate[0][0]
    hx=coordinate[2][0]
    ly=coordinate[0][1]
    hy=coordinate[1][1]


    r=hy+2
    textthreshold=5


    threshold=2
    flag=1
    v=0
    count=0
    xcoord=[]
    r1=0
    r2=0
    check=0

    while (flag==1):
        v=0
        for c in range (lx,hx):
            
            if img[r,c]==0 :
                v=v+1
        

        if v>textthreshold:
            count = count+1
            if check==0 :
                r1=r
            check=1
        if(v<textthreshold):
            v=0
            r2=r
            check=0
            if count >threshold :
                xcoord.append([r1 - pad,r2 + pad])
            count =0
            if len(xcoord)==3 :
                break
         
        
        
        r=r+1
        if r-hy>200 or r>img.shape[0]-3:
            flag=0 
    '''    print "v",v,"count",count,"r",r
        print check '''
    
    # for i in xcoord :
    #     print i[0] , i[1]
    #     cv2.line(img,(lx,i[0]),(hx,i[0]),(10,30,80),1)    
    #     cv2.line(img,(lx,i[1]),(hx,i[1]),(10,30,80),1)
    # showimg(img)

    c=lx
    flag=1
    v=0
    ycoord=[]
    count=0
    check
    textarea=0
    c1=0
    c2=0
    prev_gap=0
    gap=0
    mingap=5
    textarea=0
    while flag==1:
        for r in range( ly,hy):
            if img[r,c]==0 :
                v=v+1

        if v>textthreshold:
            if textarea==0 and count>3:
                textarea=1            
            count=count+1
            if check==0:
                c1=c
                prev_gap=gap
                if gap<mingap and textarea==1:
                    y=len(ycoord)
                    c1=ycoord[y-1][1]
                    ycoord.pop()
            if count>2:
                gap=0
            check=1
            
        if v<textthreshold:
            
                
            if count>threshold :
                ycoord.append([c - pad ,c1 + pad])
            if check==1 and count>2:
                    gap=0
            gap=gap+1
            check=0
            count=0
        if c==1 or len(ycoord)==2:
            flag=0

        c=c-1
        v=0

           
    return (xcoord,ycoord)   

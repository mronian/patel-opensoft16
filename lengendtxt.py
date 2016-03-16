import numpy as np
import cv2
def legendtextcorner(img,coordinate):
    
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    k,img = ret,thresh1 = cv2.threshold(img,200,255,cv2.THRESH_BINARY)
    lx=coordinate[0][0]
    hx=coordinate[2][0]
    ly=coordinate[0][1]
    hy=coordinate[1][1]

    c=hx-1
    v=0
    total=0
    a=[]
    img1=img

    while c>lx:
        
        for r in range(ly,hy):
            if img[r][c]==0:
                v=v+1
        
        total=total+v
        a.append(v)
        
        v=0
        c=c-1

    r=1.2
    avg=total*r/(hx-lx)
    avg=int(avg)
    
    gap=0
    count=0
    gapthresh=10
    thresh=50
    check=0
    c1=0
    c2=0
    i=0
    flag=0
    buff=5
    t1=0
    t2=0
    t=0
    w=0

    for i in range (0,hx-lx-2):
        if a[i]>=avg :
            count=count+1
            if(check==0) and gap>gapthresh :
                c1=hx-1-i
            if count >20:
                gap=0
            check=1
        if a[i]<avg :
            gap=gap+1
            
            if gap>gapthresh:
                if count>thresh:
                    c2=hx-1-i+gapthresh
                    break
                count=0
                check=0

    

    print c1,c2

    r=0
    v=0
    buff=70
    flag=0
    t1=0
    t2=0
    t=0
    vprev=0
    f=0
    while(flag<2) and r<30:
        v=0
        for c in range(lx,hx):
            if img[r][c]==0:
                v=v+1
        
        if v>30:
            f=1
        if r>0 and f==1:
            if abs(vprev-v)>buff:
                
                flag=flag+1
                if flag==1:
                    t1=r
                    
                    
                    w=t1
                    buff=5
                if flag==2:
                    t2=r
                    
                    
                    t=abs(t1-t2)
                   
                    break
        vprev=v
        r=r+1
            


    b=[]
    v=0
    i=0

    for r in range(t2,hy-t2):
        for c in range (c2,c1):

            if img[r][c]==0:
                v=v+1
        
        b.append(v)
        
        v=0

    ypixthresh=10
    ythresh=20
    ygapthresh=10
    i=0
    check=0
    gap=0
    r1=0
    r2=0
    count=0

    for i in range(0,hy-t2-t2-1):
        if b[i]>=ypixthresh :
            count=count+1
            if(check==0) and gap>min(ygapthresh,i-1) :
                r1=i+t2
            if count >7:
                gap=0
            check=1
        if b[i]<ypixthresh :
            gap=gap+1
            
            if gap>ygapthresh:
                if count>ythresh:
                    r2=i-ygapthresh+t2
                    break
                count=0
                check=0

    return [[c2,r1],[c2,r2],[c1,r2],[c1,r1]]
    




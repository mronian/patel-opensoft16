import cv2

def findCorners_1(img):

    gray = img.gray

    ret,thresh = cv2.threshold(gray,127,255,1)

    contours,h = cv2.findContours(thresh,1,2)



    for cnt in contours:
        approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)

        if len(approx)==4:
            if cv2.contourArea(cnt) > 283060.0 :
                out = approx


    return out

import cv2

class Image():
    img = None
    gray = None

    def __init__(self, imgpath):

        self.img = cv2.imread(imgpath)
        self.gray = cv2.imread(imgpath,0)

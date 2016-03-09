import cv2

class Image():
    img = None
    gray = None

    def __init__(self, imgpath):

        self.imgpath = imgpath
        self.reload()


    def reload(self):
        imgpath = self.imgpath
        self.img = cv2.imread(imgpath)
        self.gray = cv2.imread(imgpath,0)
        self.hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)

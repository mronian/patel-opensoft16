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

    def init_test_vals(self):

        self.corners = [

            [145,  87],

            [145, 536],

            [860, 536],

            [860,  87],
        ]

        lgnd = [
                [314,623],[314,839],[520,839],[520,623]
        ]
        
        self.legend_corners = []
        for cr in lgnd:
            self.legend_corners.append(list(reversed(cr)))


        self.first_xtick = [240,538]
        self.first_ytick = [145, 136]
        self.first_tick_text = "500"
        self.xticks = [
            (240, 538),
            (333, 538), 
        ]
        self.colors = {
            (48 ,31, 188),
            (90, 182, 109),
            (148, 81, 72),
            (135, 102, 159),
            (213, 201, 129),
            (59, 235, 241),
            (170, 170, 170)
        }
        self.plot_title = r'b) Performances of various anytime algorithms'
        self.x_caption = r'Time (Sec)'
        self.y_caption = r'% Optimal Closeness'
        self.pltclr = 177

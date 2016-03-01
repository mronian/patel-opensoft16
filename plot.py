import corners

methods = {

        "cornerFinder": corners.findCorners_1,
        "seriesPointsFinder": None

}

class Plot():

    img = None # openCV object
    corners = [] # Boundary corners
    seriesPoints = {} # Series Points


    def __init__(self, img):
        self.img = img

    def findCorners(self):
        """
        Input: img
        Output: corners
        """
        assert self.img != None
        self.corners = methods["cornerFinder"](self.img)
        assert len(self.corners) != 0



    def findSeriesPoints(self):

        assert len(self.corners) != 0
        self.seriesPoints = methods["seriesPointsFinder"](self.img, self.corners)
        assert len(self.seriesPoints) != 0

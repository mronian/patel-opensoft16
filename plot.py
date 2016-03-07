from plotmethods import methods

class Plot():

    img = None # openCV object
    corners = [] # Boundary corners
    seriesPoints = {} # Series Points
    colors = {} # Set of color tuples present in the plot

    X_scale = (0,0)
    Y_scale = (0,0)


    def __init__(self, img):
        self.img = img

    def findCorners(self):
        """
        Input: 
            Plot Image
        Output: 
            Corners
        """
        assert self.img != None
        self.corners = methods["cornerFinder"](self.img)
        assert len(self.corners) != 0

        return self.corners

    def findTicks(self):
        """
        Input: 
            Plot Image
            Corners
        Output: 
            X_ticks - Array of coordinates of ticks
            Y_ticks - Array of coordinates of ticks
        """

        self.x_ticks, self.y_ticks = methods["ticksFinder"](self.img, self.corners)
        return self.x_ticks

    def findTickText(self):

        self.xticksTextRects = methods["xtickstextFinder"](self.img, self.corners, self.x_ticks)
        return self.xticksTextRects

    def findSeriesPoints(self):
        """
        Input: 
            Plot Image
            Corners
        Output: 
            Series Points with Colors
        """
        assert len(self.corners) != 0
        self.seriesPoints = methods["seriesPointsFinder"](self.img, self.corners)
        # assert len(self.seriesPoints) != 0

    def recognizeText(self):
        """
        Find all text portions in the image and output 
        a dictionary with text bounding rectangle corner 
        cordinates as the key and the actual text as value

        Input: 
            Plot Image
            Regions
        Output: 
            Dict(Region -> Text)
        """
        pass
    
    def findColors(self):
        """
        Input:
            Legend Corners
        Output:
            Set of tuples of colors present in the plot
        """
        self.colors = methods["colorFinder"](self.img, self.legend_corners)
        return self.colors

    def maskColor(self, color):

        self.maskedImage = methods["maskColor"](self.img.img, self.corners, color)
        return self.maskedImage


    def parseScaleValues(self):
        """
        Input: 
            PlotInfo
        Output: 
            X_Scale - (m,b) xnew = xold*m + b
            Y_Scale - (m,b) ynew = yold*m + b
        """
        pass

    def rescaleSeries(self):
        """
        Input: 
            SeriesPoints
            X_Scale, Y_Scale
        Output: 
            ScaledSeriesPoints
        """
        pass

    """
    The next functions use Text areas calculated from assignTextRoles() function
    We just have to return those Text Areas by these functions
    """
    def findTitleRect():
        """
        Input:
            None
        Output:
            Rectangle surrounding the Plot Title
        """
        pass

    def findXCaptionRect():
        """
        Input:
            None
        Output:
            Rectangle surrounding the X-axis Caption
        """
        pass

    def findYCaption():
        """
        Input:
            None
        Output:
            Rectangle surrounding the Y-axis Caption
        """
        pass
        

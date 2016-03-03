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

        self.x_ticks = methods["xticksFinder"](self.img, self.corners)
        return self.x_ticks

    def find_tick_text(self):

        self.xticksTextRects = methods["xtickstextFinder"](self.img, self.corners, self.xticks)
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

    def assignTextRoles(self):
        """
        For each text region, assign its role in the plot
        PlotInfo:
            1. Plot Caption
            2. X-Axis Label
            3. Y-Axis Label
            4. Legends
            5. X-Axis Ticks
            6. Y-Axis Ticks

        Input: 
            Plot Image
            Dict(Region -> Text)
        Output: 
            PlotInfo
        """
        pass
    
    def findColors(self):
        """
        Input:
            Plot Corners
        Output:
            Set of tuples of colors present in the plot
        """
        self.colors = methods["colorFinder"](self.img)
        return self.colors

        pass
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

    def findTitleRect():
        """
        
        """
        pass
    def findXCaptionRect():
        """
        
        """
        pass
    def findYCaption():
        """
        
        """
        pass
        
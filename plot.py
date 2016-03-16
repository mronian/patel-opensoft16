from plotmethods import methods
import numpy as np
import cv2
import helpers
from getbounds import getbounds

class Plot():

    img = None # openCV object
    corners = [] # Boundary corners
    seriesPoints = {} # Series Points
    colors = {} # Set of color tuples present in the plot

    scale_x = (1,0,10)
    scale_y = (-1,0)
    allPlots = {}

    legend_corners = []

    def __init__(self, img):
        self.img = img

    def findCorners(self):
        """
        Input: 
            Plot Image
        Output: 
            Corners
        """
        print "Finding all Corners"
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

        print "Finding Tick Coordinates"
        self.x_ticks, self.y_ticks = methods["ticksFinder"](self.img, self.corners)
        return self.x_ticks

    def findTickText(self):

        print "Finding X Tick Digits Bounding Rects"
        # self.getBounds()
        self.xticksTextRects = methods["xtickstextFinder"](self.img.img, self.corners, self.x_ticks, self.bounds)
        return self.xticksTextRects

    def findyTickText(self):

        print "Finding Y Tick Digits Bounding Rects"
        # self.getBounds()
        self.yticksTextRects = methods["ytickstextFinder"](self.img.img, self.corners, self.y_ticks, self.bounds)
        return self.yticksTextRects

    def parseScaleValues(self):
        """
        Input: 
            PlotInfo
        Output: 
            X_Scale - (m,b) xnew = xold*m + b
            Y_Scale - (m,b) ynew = yold*m + b
        """
        print "Parsing Scale Values"
        self.scale_x = methods["parseScale"](self.img, self.corners, self.x_ticks, self.xticksTextRects, True)
        self.scale_y = methods["parseScale"](self.img, self.corners, self.y_ticks, self.yticksTextRects, False)
        return self.scale_x

    def rescaleSeries(self, series):
        """
        Input: 
            SeriesPoints
            X_Scale, Y_Scale
        Output: 
            ScaledSeriesPoints
        """
        return methods["rescale"](series, self.corners, self.scale_x, self.scale_y)

    def findSeriesPoints(self, img):
        """
        Input: 
            Plot Image
            Corners
        Output: 
            Series Points with Colors
        """
        assert len(self.corners) != 0
        return methods["seriesPointsFinder"](img, self.corners)
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
        
    def getColorQuant(self):

        print "Finding all Colours and Plot Series"

        self.allPlots = methods["colorQuantization"](self.img, self.corners)
        return self.allPlots

    def extractPlotLine(self, color):
        self.pltline = methods["plotLineExtractor"](self.img, self.corners, self.legend_corners, color)
        return self.pltline

    def getAllSeries(self):

        print "Interpolating missing values and Rescaling"

        out = {}
        
        for k in self.allPlots.keys():
            plot = self.allPlots[k]

            points = self.findSeriesPoints(plot[2])
            # points = np.array(plot[0])
            # points += self.corners[0]
            if len(points) == 0:
                continue
            scaledPoints = self.rescaleSeries(points)
            out[k] = scaledPoints
            print out[k].tolist()
            # helpers.plotPoints(self.img.img, points)

        self.allScaledSeries = out
        return out


    def findLegendCorners(self):

        self.legend_corners = methods["findLegend"](self.img, self.corners, self.allPlots)


    def show_ticks(self):
        helpers.plotPoints(self.img.img, self.x_ticks)
        helpers.plotPoints(self.img.img, self.y_ticks)

    def show_ticktexts(self):
        for rect in self.yticksTextRects:
            helpers.plotPoints(self.img.img, rect)
            try:
                print helpers.getOCRText(self.img.img, rect)
            except:
                pass

        for rect in self.xticksTextRects:
            helpers.plotPoints(self.img.img, rect)
            print helpers.getOCRText(self.img.img, rect)

    def show_corners(self):
        helpers.plotPoints(self.img.img, self.corners)
        # helpers.plotPoints(self.img.img, self.legend_corners)

    def plotCheck(self):

        print "Checking if the rectangle is a plot"

        self.is_plot = methods["plotCheck"](self.img, self.corners)
        return self.is_plot

    def getBounds(self):

        self.bounds = getbounds(self.img.img, self.corners)

    def getAxisCaption(self):

        y1, y2 = self.bounds[0][2]
        x1, x2 = self.corners[0][0], self.corners[2][0]
        x1 -= 5
        x2 += 5
        
        xaxisCorenrs = [
                (x1, y1),
                (x1, y2),
                (x2, y2),
                (x2, y1),
        ]
        self.plot_caption = helpers.getOCRText(self.img.img, xaxisCorenrs, "-psm 7")

        y1, y2 = self.bounds[0][1]
        x1, x2 = self.corners[0][0], self.corners[2][0]
        x1 -= 5
        x2 += 5
        
        xaxisCorenrs = [
                (x1, y1),
                (x1, y2),
                (x2, y2),
                (x2, y1),
        ]
        self.x_caption = helpers.getOCRText(self.img.img, xaxisCorenrs, "-psm 7")
        # helpers.plotPoints(self.img.img, xaxisCorenrs)

        x1, x2 = self.bounds[1][1]
        y1, y2 = self.corners[0][1], self.corners[1][1]
        x1 -= 5
        x2 += 5
        xaxisCorenrs = [
                (x1, y1),
                (x1, y2),
                (x2, y2),
                (x2, y1),
        ]
        img = helpers.getSubImage(self.img.gray, xaxisCorenrs)
        dst = img.transpose()
        dst = cv2.flip(dst, 1)
        self.y_caption = helpers.getOCRText(dst, None, "-psm 7")


    def generate_output(self):

        allplts = []
        for k in self.allScaledSeries.keys():
            val = self.allScaledSeries[k]

            # plt = (self.legends[k], val)
            plt = ("plot_%d"%k, val.tolist())
            allplts.append(plt)
        
        out = (
                self.plot_caption,
                self.x_caption,
                self.y_caption,
                allplts
        )
        return out




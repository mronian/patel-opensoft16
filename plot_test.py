import unittest
from plot import *
from image import *
import cv2
import helpers as helper
import matplotlib.pyplot as plt

class TestPlot(unittest.TestCase):

    def setUp(self):
        img = Image("img/tstplot.jpg")
        self.plot = Plot(img)
        self.initialize_hardcoded_values()

    def initialize_hardcoded_values(self):

        self.corners = [

            [145,  87],

            [145, 536],

            [860, 536],

            [860,  87],
        ]
        self.legend_corners = [

            [145,  87],

            [145, 536],

            [860, 536],

            [860,  87],
        ]
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

    def test_finding_corners(self):
        """
        Setup: 
            - Input Test Image (Already done)
        
        Assertion:
            - Compare the area of contour with the actual area
        
        Things to Find:
            - Area of Bounding Rectangle
            
        """
        self.plot.findCorners()
        assert cv2.contourArea(self.plot.corners) > 321000

    def test_xtick_coordinates(self):
        """
        Setup: 
            - Input Test Image (Already done)
            - Corners
        
        Assertion:
            - Check if the calculated 1st tick point is approximately correct
        
        Things to Find:
            - Corner Points
            - Actual Coordinates of the 1st tick point
            
        """

        self.plot.corners = self.corners
        self.plot.findTicks()
        ticks = self.plot.x_ticks
        assert helper.getDistance(ticks[1], self.first_xtick) < 5

    def test_ytick_coordinates(self):
        """
        Setup: 
            - Input Test Image (Already done)
            - Corners
        
        Assertion:
            - Check if the calculated 1st tick point is approximately correct
        
        Things to Find:
            - Corner Points
            - Actual Coordinates of the 1st tick point
            
        """

        self.plot.corners = self.corners
        self.plot.findTicks()
        ticks = self.plot.y_ticks
        assert helper.getDistance(ticks[1], self.first_ytick) < 5

    def test_xtick_text(self):
        """
        Setup: 
            - Input Test Image (Already done)
            - Corners
            - 1st Tick Point Coordinates
        
        Assertion:
            - Check the OCR on bounding rect and match it with actual text
        
        Things to Find:
            - Corner Points
            - Actual Coordinates of the 1st tick point
            - Actual text content corresponding to 1st tick
            
        """

        self.plot.corners = self.corners
        # self.plot.x_ticks = self.xticks
        self.plot.findTicks()
        ticktextRect = self.plot.findTickText()
        tickText = helper.getOCRText(self.plot.img.img, ticktextRect[1])
        
        assert tickText == self.first_tick_text

    def test_ytick_text(self):
        """
        Setup: 
            - Input Test Image (Already done)
            - Corners
            - 1st Tick Point Coordinates
        
        Assertion:
            - Check the OCR on bounding rect and match it with actual text
        
        Things to Find:
            - Corner Points
            - Actual Coordinates of the 1st tick point
            - Actual text content corresponding to 1st tick
            
        """

        self.plot.corners = self.corners
        # self.plot.x_ticks = self.xticks
        self.plot.findTicks()
        ticktextRect = self.plot.findyTickText()
        # import pdb; pdb.set_trace()
        tickText = helper.getOCRText(self.plot.img.img, ticktextRect[1])
        
        assert tickText == "90"
    """
    TODO: This test_finding_seriespoints function is not complete yet
    """
    def test_finding_seriespoints(self):
        """
        Setup: 
            - Input Test Image (Already done)
            - Corners
            - Tick Coordinates
        
        Assertion:
            - Check the Series points with the hardcoded series points
        
        Things to Find:
        """
        self.plot.corners = self.corners
        img = Image("img/series_green.jpg") 
        points = self.plot.findSeriesPoints(img)
        print points
        helper.plotPoints(self.plot.img.img, points)

    def test_extract_plot_colors(self):
        """
        Setup: 
            - Input Test Image (Already done)
        
        Assertion:
            - Check the colors present in Image with hardcoded colors
        
        Things to Find:
            - Set of tuples of colors (except Black and white) in Image
        """
        self.plot.corners = self.corners
        self.plot.legend_corners = self.legend_corners
        plotColors = self.plot.findColors()
        assert plotColors == self.colors

    
    def test_extract_plot_title(self):
        """
        Setup: 
            - Input Test Image (Already done)
            - Corners
        Assertion:
            - Check the plot title with hardcoded value
        
        Things to Find:
            - Rect surrounding the plot title
            - plot title from the Rect
        """
        self.plot.corners = self.corners
        plotTitleRect = self.plot.findTitleRect()
        plotTitle = helper.getOCRText(self.plot.img, plotTitleRect)
        assert plotTitle == self.plot_title

    def test_extract_xaxis_caption(self):
        """
        Setup: 
            - Input Test Image (Already done)
            - Corners
        Assertion:
            - Check the x-axis caption with hardcoded value
        
        Things to Find:
            - Rect surrounding the x-axis caption
            - x-axis caption from the Rect
        """
        self.plot.corners = self.corners
        xaxisCaptionRect = self.plot.findXCaptionRect()
        xaxisCaption = helper.getOCRText(self.plot.img, xaxisCaptionRect)
        assert xaxisCaption == self.x_caption


    def test_extract_yaxis_caption(self):
        """
        Setup: 
            - Input Test Image (Already done)
            - Corners
        Assertion:
            - Check the y-axis caption with hardcoded value
        
        Things to Find:
            - Rect surrounding the y-axis caption
            - y-axis caption from the Rect
        """
        self.plot.corners = self.corners
        yaxisCaptionRect = self.plot.findYCaption()
        yaxisCaption = helper.getOCRText(self.plot.img, yaxisCaptionRect)
        assert yaxisCaption == self.y_caption

    def test_mask_other_colors(self):
        """
        Setup: 
            - Input Test Image (Already done)
            - Corners
            - Target Color
            - All Colors
        Assertion:
            - Check the masked out version of image is correct
        Things to Find:
            - Masked out version of plot wrt each color in plot
        """
        self.plot.corners = self.corners
        
        clr = (88,79,223)

        img = self.plot.maskColor(clr)
        plt.show(img)
        cv2.imshow("input", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        for target_color in self.colors:
            maskedPlot = helper.getMaskedPlot(self.plot.img, target_color, self.colors)
            for color in self.colors:
                if color == target_color:
                    if color not in maskedPlot:
                        assert False
                elif color != target_color:
                    if color in maskedPlot:
                        assert False
        assert True


    def test_color_quantization(self):
        self.plot.corners = self.corners
        img = self.plot.getColorQuant()
        helper.showimg(img)

# unittest.main()

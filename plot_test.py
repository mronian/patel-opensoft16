import unittest
from plot import *
from image import *
import cv2
import helpers as helper

class TestPlot(unittest.TestCase):

    def setUp(self):
        img = Image("img/tstplot.jpg")
        self.plot = Plot(img)
        self.initialize_hardcoded_values()

    def initialize_hardcoded_values(self):

        self.corners = [

            [[145,  87]],

            [[145, 536]],

            [[860, 536]],

            [[860,  87]],
        ]
        self.first_tick = [240,538]
        self.first_tick_text = 500
        self.xticks = [
            (240, 538),
            (333, 538), 
        ]
        self.colors = [
            (48 ,31, 188),
            (90, 182, 109),
            (148, 81, 72),
            (135, 102, 159),
            (213, 201, 129),
            (59, 235, 241),
            (170, 170, 170)
        ]

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

        ticks = self.plot.findTicks()
        assert helper.getDistance(ticks[0], self.first_tick) < 5


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
        self.plot.xticks = self.xticks
        ticktextRect = self.plot.find_tick_text()
        
        tickText = helper.getOCRText(self.plot.img, ticktextRect[0])
        assert tickText == self.first_tick_text

    def test_finding_seriespoints(self):
        """
        
        """
        self.plot.corners = self.corners
        self.plot.findSeriesPoints()
        print self.plot.seriesPoints

    def test_extract_plot_colors(self):
        """
        
        """
        self.plot.corners = self.corners
        plotColors = self.plot.findColors()
        assert plotColors == set(self.colors)

    def test_extract_xaxis_caption(self):
        """
        
        """
        pass

    def test_extract_yaxis_caption(self):
        """
        
        """
        pass

    def test_mask_other_colors(self):
        """
        
        """
        pass

unittest.main()
